# AI-Powered Visual Property Search and Real Estate Discovery Platform

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/) 
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green)](https://fastapi.tiangolo.com/) 
[![React](https://img.shields.io/badge/React-18.2.0-blue)](https://reactjs.org/) 
[![MUI](https://img.shields.io/badge/MUI-5.14.11-purple)](https://mui.com/) 
[![FAISS](https://img.shields.io/badge/FAISS-1.7.4-red)](https://github.com/facebookresearch/faiss) 
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

---

## Project Overview

**HomeVision AI** is an AI-powered real estate search platform that allows users to **find visually similar properties** by uploading images.  

It combines **image embeddings, vector search, and modern frontend design** to create a fast, scalable, and user-friendly platform. Designed for **global use**, it supports future cloud deployment, subscription plans, and multi-region search.

---

## Key Features

- **AI-Powered Visual Search:** Upload a property image and find similar listings.  
- **Advanced Filters:** Search by price, city, country, or other property attributes.  
- **Professional UI/UX:** Responsive frontend with React.js + MUI.  
- **Vector Search Engine:** Local FAISS or cloud-based Pinecone/Weaviate.  
- **Cloud-Ready Storage:** Supports AWS S3 or Google Cloud Storage for images.  
- **Search History Tracking:** Keep user search history in a scalable database.  
- **Extensible Architecture:** Ready for SaaS monetization and global scaling.  

---

## Tech Stack

**Frontend:**  
- React.js 18  
- MUI 5 (Material UI)  
- Axios  

**Backend:**  
- FastAPI  
- Python 3.11  
- SQLAlchemy (SQLite for MVP, Postgres for production)  
- FAISS (local vector search) / Pinecone (cloud scalable)  
- PIL / OpenCV (image preprocessing)  

**Cloud & Deployment (Future):**  
- AWS S3 / Google Cloud Storage  
- Render.com / AWS EC2 / Google Cloud  
- Stripe (subscription management)  

---

## Architecture

```text
User (Web / Mobile)
      |
      v
Frontend (React + MUI)
      |
      v
Backend (FastAPI)
      |
      +--> Database (SQLite / Postgres)
      |
      +--> Vector Store (FAISS / Pinecone)
      |
      +--> Image Storage (Local / S3)

```

**Clone Repository**

```
git clone https://github.com/yourusername/visual-home-finder.git
cd visual-home-finder
```

**Backend Setup**

```
cd backend
python -m venv env
.\env\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

**Frontend Setup**

```
cd ../frontend
npm install
npm run dev
```

### Roadmap

- Integrate Pinecone / Weaviate for scalable vector search.
- Use cloud storage for all images (S3 / GCS).
- Implement user authentication + Stripe subscriptions.
- Add analytics dashboard for admins (search trends, usage stats).
- Deploy a global-ready SaaS version with multi-region support.
- Add mobile-first design for iOS/Android.

## License

This project is licensed under the [MIT License](LICENSE) – see the LICENSE file for details.
