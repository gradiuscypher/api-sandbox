"""
example dependencies for my API
"""

from typing_extensions import Annotated

from fastapi import Header, HTTPException, status

from api_sandbox.api.models import Item


class ItemNameChecker:
    """
    Checks if we were given a special item in our POST request
    """

    def __init__(self, item_name: str):
        self.item_name = item_name

    def __call__(self, item: Item):
        if item.name == self.item_name:
            return True

        return False


class HeaderAuth:
    """validates authentication based on a header"""

    def __init__(self, api_key: str):
        self.api_key = api_key

    def __call__(self, x_key: Annotated[str, Header()] = ""):
        if not x_key:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Please provide an API key in the x-key header",
            )
        if x_key != self.api_key:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key"
            )
