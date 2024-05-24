from enum import Enum

from pydantic import BaseModel

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def index():
    return {"items": "David"}

@app.get("/items/{item_id}")
def query_item_by_id(item_id: int):
    return {"item_id" : item_id}