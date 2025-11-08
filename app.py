from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a simple Pydantic model for POST request body
class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "GET request successful!"}

@app.post("/items/")
def create_item(item: Item):
    return {
        "message": "POST request successful!",
        "data_received": item
    }
