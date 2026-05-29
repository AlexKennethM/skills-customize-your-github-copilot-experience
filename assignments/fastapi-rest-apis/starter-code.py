from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

items = []

@app.get("/items/")
def list_items(limit: int = 10, available: Optional[bool] = None):
    """Return a list of items, optionally filtered by availability."""
    filtered = items
    if available is not None:
        filtered = [item for item in items if item["in_stock"] == available]
    return filtered[:limit]

@app.post("/items/", status_code=201)
def create_item(item: Item):
    """Create a new item and return it with a generated id."""
    item_data = item.dict()
    item_data["id"] = len(items) + 1
    items.append(item_data)
    return item_data

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Return a single item by its ID."""
    for item in items:
        if item["id"] == item_id:
            return item
    return {"detail": "Item not found"}
