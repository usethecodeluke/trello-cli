import sys
from typing import List, Optional
from typing_extensions import Annotated

import typer
from rich.console import Console

from config import get_config
from client import TrelloClient
from utils import render_card, render_board_list

console = Console()
config = get_config()
if not all([config.api_key, config.api_token]):
    console.print(
        """
:exclamation:API_KEY and API_TOKEN environment variables must be set.:exclamation:
The variables may be set in the environment directly or through a .env file.
Please see the README.md file for more info.
"""
    )
    sys.exit(1)

app = typer.Typer(no_args_is_help=True)
client = TrelloClient(
    api_key=config.api_key,
    api_token=config.api_token,
    api_url=config.api_url,
)


@app.callback()
def callback():
    """
    A simple CLI for interacting with Trello Cards.
    """


@app.command()
def get_boards(is_json: Annotated[bool, typer.Option("--json")] = False) -> None:
    """
    Fetch all Trello boards for the authenticated user.
    """
    result = client.get_boards()
    if is_json:
        console.print_json(data=result)
        return
    render_board_list(result)


@app.command()
def get_board(board_id: Annotated[str, typer.Argument()]) -> None:
    """
    Fetch a Trello board by id.
    """
    pass


@app.command()
def get_lists(board_id: Annotated[str, typer.Argument()]) -> None:
    """
    Fetch the Trello lists for a given board id.
    """
    pass


@app.command()
def get_list(list_id: Annotated[str, typer.Argument()]) -> None:
    """
    Fetch a Trello list by id.
    """
    pass


@app.command()
def get_card(
    card_id: Annotated[str, typer.Argument()],
    is_json: Annotated[bool, typer.Option("--json")] = False,
) -> None:
    """
    Fetch a card using the id field.
    """
    result = client.get_card(card_id)
    if is_json:
        console.print_json(data=result)
        return
    render_card(result)


@app.command()
def create_card(
    title: Annotated[str, typer.Argument()],
    body: Annotated[str, typer.Argument()],
    labels: Annotated[List[str], typer.Option()],
    comments: Annotated[List[str], typer.Option()],
) -> None:
    """
    Create a new card on a Trello board.
    """
    pass


@app.command()
def add_card_labels(
    card_id: Annotated[str, typer.Argument()],
    labels: Annotated[List[str], typer.Argument()],
) -> None:
    """
    Attach labels to a card.
    """
    pass


if __name__ == "__main__":
    app()
