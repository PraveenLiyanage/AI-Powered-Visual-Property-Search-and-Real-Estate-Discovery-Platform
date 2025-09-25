import requests

listings = [
    {"title":"Modern Villa","price":350000,"image_url":"https://images.unsplash.com/photo-1600585154340-be6161a56a0c","city":"Los Angeles","country":"USA"},
    {"title":"Cozy Cottage","price":120000,"image_url":"https://images.unsplash.com/photo-1579690602005-647035ff79c3?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","city":"Portland","country":"USA"},
    {"title":"Luxury Penthouse","price":950000,"image_url":"https://images.unsplash.com/photo-1570129477492-45c003edd2be","city":"New York","country":"USA"},
    {"title":"Beach House","price":500000,"image_url":"https://images.unsplash.com/photo-1505691938895-1758d7feb511","city":"Miami","country":"USA"},
    {"title":"Mountain Cabin","price":220000,"image_url":"https://images.unsplash.com/photo-1551648746-d158bcd704e7?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","city":"Denver","country":"USA"},
    {"title":"Urban Apartment","price":300000,"image_url":"https://images.unsplash.com/photo-1611095210561-67f0832b1ca3?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","city":"London","country":"UK"},
    {"title":"Minimalist House","price":400000,"image_url":"https://images.unsplash.com/photo-1580587771525-78b9dba3b914?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D","city":"Tokyo","country":"Japan"},
    {"title":"Villa with Pool","price":650000,"image_url":"https://images.unsplash.com/photo-1568605114967-8130f3a36994","city":"Dubai","country":"UAE"},
    # Add 20–30 more similar entries...
]

for item in listings:
    try:
        resp = requests.post("http://127.0.0.1:8000/ingest", data=item, timeout=10)
        print(resp.json())
    except Exception as e:
        print("Failed:", item["title"], e)
