from typing import List, Optional
from typing_extensions import Annotated

import typer

from client import TrelloClient


app = typer.Typer()


@app.callback()
def callback():
    """
    A simple CLI for interacting with Trello Cards.
    """


@app.command()
def get_card(board: str):
    pass

@app.command()
def create_card(
    title: Annotated[str],
    body: Annotated[str],
    labels: Annotated[List[str]],
    comments: Annotated[List[str]],
    ):
    pass

@app.command()
def add_card_labels(card_id: str, labels: List[str]):
    pass