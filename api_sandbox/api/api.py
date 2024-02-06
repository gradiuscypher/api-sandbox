"""
A basic API playground written with FastAPI
"""

from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI

from api_sandbox.api.models import Item
from api_sandbox.api.dependencies import ItemNameChecker, HeaderAuth

app = FastAPI()
special_item_check = ItemNameChecker("special")


@app.get("/")
async def root():
    """
    the root API endpoint
    """
    return {"message": "Hello world!"}


@app.get("/items/{item_id}")
async def get_item(item_id: int, q: str | None = None):
    """
    get an item ID and the query parameters and return them as JSON
    """
    return {"item_id": item_id, "q": q}


@app.post("/items/special")
async def special_item(
    item: Item, is_special: Annotated[bool, Depends(special_item_check)]
):
    """
    an example route with Depends check
    """
    return {
        "item_name": item.name,
        "item_desc": item.description,
        "item_price": item.price,
        "is_special": is_special,
    }


@app.get("/protected", dependencies=[Depends(HeaderAuth("TESTKEY123"))])
async def protected_info():
    """
    an example route protected by depends
    """
    return {"message": "Nice API key"}


def main():
    """run the api"""
    uvicorn.run(app)
