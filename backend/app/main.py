from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .db import SessionLocal, engine, Base
from .models import Property
from .embeddings import CLIPEmbedder
from .vector_store import FaissStore
from PIL import Image
import io
import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# create tables
Base.metadata.create_all(bind=engine)

embedder = CLIPEmbedder()
vector_store = FaissStore(dim=512)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/ingest")
def ingest_listing(
    title: str = Form(...),
    price: float = Form(None),
    image_url: str = Form(...),
    city: str = Form(None),
    country: str = Form(None)
):
    resp = requests.get(image_url, stream=True, timeout=10)
    if resp.status_code != 200:
        raise HTTPException(status_code=400, detail="Image download failed")
    img = Image.open(io.BytesIO(resp.content)).convert("RGB")

    vec = embedder.image_to_vector(img)

    db = next(get_db())
    prop = Property(title=title, price=price, image_url=image_url, city=city, country=country)
    db.add(prop)
    db.commit()
    db.refresh(prop)

    vector_store.add(vec, prop.id)
    return {"ok": True, "property_id": prop.id}

@app.post("/search")
def search_image(file: UploadFile = File(...), top_k: int = 6):
    contents = file.file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    vec = embedder.image_to_vector(img)
    hits = vector_store.search(vec, top_k=top_k)

    db = next(get_db())
    results = []
    for hit in hits:
        prop = db.query(Property).filter(Property.id == hit['property_id']).first()
        if prop:
            results.append({
                "property_id": prop.id,
                "title": prop.title,
                "price": prop.price,
                "city": prop.city,
                "country": prop.country,
                "image_url": prop.image_url,
                "score": hit['score']
            })
    return {"results": results}
