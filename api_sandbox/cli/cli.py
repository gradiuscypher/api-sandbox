from typing import Optional
from typing_extensions import Annotated

import httpx
import typer

from api_sandbox.api.models import Item

app = typer.Typer()
client = httpx.Client(base_url="http://localhost:8000")


@app.command()
def create_special(
    name: Annotated[str, typer.Argument(help="Required item name")],
    price: Annotated[float, typer.Argument],
    description: Annotated[
        Optional[str], typer.Argument(help="Optional item description")
    ] = "Default description",
):
    """
    create a special item
    """
    item = Item(name=name, description=description, price=price)
    r = client.post("/items/special", json=item.model_dump())
    print(r.json())


@app.command()
def protected(
    should_pass: Annotated[bool, typer.Option("--pass")] = False,
    empty: Annotated[bool, typer.Option("--empty")] = False,
):
    """
    test a protected API
    """
    if empty:
        r = client.get("/protected")
        print(r.status_code, r.text)

    elif should_pass:
        headers = {"x-key": "TESTKEY123"}
        r = client.get("/protected", headers=headers)
        print(r.json())

    else:
        headers = {"x-key": "FAILKEY"}
        r = client.get("/protected", headers=headers)
        print(r.status_code, r.json())


if __name__ == "__main__":
    app()
