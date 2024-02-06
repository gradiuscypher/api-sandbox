"""
example models for my API and CLI
"""

from pydantic import BaseModel


class Item(BaseModel):
    """
    an example item to create a model.
    """

    name: str
    description: str | None = None
    price: float
