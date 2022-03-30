from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
app = FastAPI()
import pandas as pd
from pymongo import MongoClient

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

client = MongoClient("___mongo___key")
db = client.myfoodDB
collection = db.foods
foods_data = pd.DataFrame.from_records(list(collection.find()))




def findImgUrl(keyword) :
    resp = requests.get(url="https://serpapi.com/search.json?engine=google&q={}&filter=0&tbm=isch&api_key=__serpapi_key___".format(keyword))
    data = resp.json()
    return data['images_results'][0]['original']

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your food random api."}


@app.get("/foods", tags=["foods"])
async def get_todos() -> dict:
    
    food = foods_data.sample().to_dict()
    print(food, list(food["menu"].values())[0])
    return { "data": { 'menu':list(food["menu"].values())[0], 'type':list(food["type"].values())[0], 'img': findImgUrl(list(food["menu"].values())[0]) }}