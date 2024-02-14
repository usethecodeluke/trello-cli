import sys
from enum import Enum
from typing import List, Optional
from typing_extensions import Annotated

import typer
from rich.console import Console

from config import get_config
from client import TrelloClient
from utils import (
    render_card,
    render_cards,
    render_board,
    render_list,
    render_board_list,
    render_lists_list,
    render_labels_list,
)


class Colors(str, Enum):
    green = "green",
    yellow = "yellow",
    orange = "orange",
    red = "red",
    purple = "purple",
    blue = "blue",
    sky = "sky",
    lime = "lime",
    pink = "pink",
    black = "black"


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
    
    Current capabilities allow for:\n
        - Listing boards, lists, and cards\n
        - Viewing a board, list, or card\n
        - Adding a new list to a board\n
        - Adding a new card to a list / board\n
        - Commenting on a card\n
        - Adding labels to a card\n

    No delete or move functionality has been implemented yet.
    """


@app.command()
def get_boards(is_json: Annotated[bool, typer.Option("--json", help="render output in JSON")] = False) -> None:
    """
    Fetch all Trello boards for the authenticated user.
    """
    result = client.get_boards()
    if is_json:
        console.print_json(data=result)
        return
    render_board_list(result)


@app.command()
def get_board(
    board_id: Annotated[str, typer.Argument(help="the board id")],
    is_json: Annotated[bool, typer.Option("--json", help="render output in JSON")] = False,
) -> None:
    """
    Fetch a Trello board by id.
    """
    board = client.get_board_by_id(board_id)
    lists = client.get_lists_by_board_id(board_id)
    cards = client.get_cards_by_board_id(board_id)
    comments = client.get_comments_by_board_id(board_id)
    for comment in comments:
        for card in cards:
            if not "commentData" in card.keys():
                    card["commentData"] = []
            if comment["data"]["card"]["id"] == card["id"]:
                card["commentData"].append(comment)
                continue
    for card in cards:
        for x in lists:
            if not "cardData" in x.keys():
                    x["cardData"] = []
            if card["idList"] == x["id"]:
                x["cardData"].append(card)
                continue
    board["listData"] = lists
    if is_json:
        console.print_json(data=board)
        return
    lists = client.get_lists_by_board_id(board_id)
    render_board(board)


@app.command()
def get_lists(
    board_id: Annotated[str, typer.Argument(help="the board id to retrieve lists from")],
    is_json: Annotated[bool, typer.Option("--json", help="render output in JSON")] = False,
) -> None:
    """
    Fetch the Trello lists for a given board id.
    """
    lists = client.get_lists_by_board_id(board_id)
    if is_json:
        console.print_json(data=lists)
        return
    render_lists_list(lists)


@app.command()
def get_list(
    list_id: Annotated[str, typer.Argument(help="the list id")],
    is_json: Annotated[bool, typer.Option("--json", help="render output in JSON")] = False,
) -> None:
    """
    Fetch a Trello list by id.
    """
    data = client.get_list_by_id(list_id)
    cards = client.get_cards_by_list_id(list_id)
    comments = client.get_comments_by_list_id(list_id)
    for comment in comments:
        for card in cards:
            if comment["data"]["card"]["id"] == card["id"]:
                if not "commentData" in card.keys():
                    card["commentData"] = []
                card["commentData"].append(comment)
    data["cardData"] = cards
    if is_json:
        console.print_json(data=data)
        return
    render_list(data)


@app.command()
def get_cards(
    board_id: Annotated[str, typer.Argument(help="the board id to retrieve cards from")],
    list_id: Annotated[Optional[str], typer.Argument(help="optionally provide list_id to filter results by list")] = None,
    is_json: Annotated[bool, typer.Option("--json", help="render output in JSON")] = False,
) -> None:
    """
    Fetch a card using the id field.
    """
    if list_id:
        result = client.get_cards_by_list_id(list_id)
    else:
        result = client.get_cards_by_board_id(board_id)
    if is_json:
        console.print_json(data=result)
        return
    render_cards(result)


@app.command()
def get_card(
    card_id: Annotated[str, typer.Argument(help="the card id")],
    is_json: Annotated[bool, typer.Option("--json", help="render output in JSON")] = False,
) -> None:
    """
    Fetch a card using the id field.
    """
    result = client.get_card_by_id(card_id)
    comments = client.get_comments_by_card_id(card_id)
    result["commentData"] = comments
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
    is_json: Annotated[bool, typer.Option("--json", help="render output in JSON")] = False,
) -> None:
    """
    Create a new card on a Trello board.
    """
    pass


@app.command()
def get_labels(
    board_id: Annotated[str, typer.Argument(help="the board id to retrieve labels for")],
    is_json: Annotated[bool, typer.Option("--json", help="render output in JSON")] = False,
) -> None:
    """
    Fetch the labels for a given Trello board id.
    """
    labels = client.get_labels_by_board_id(board_id)
    if is_json:
        console.print_json(data=labels)
        return
    render_labels_list(labels)


@app.command()
def add_label(
    board_id: Annotated[str, typer.Argument(help="the board id to add the label to")],
    name: Annotated[str, typer.Argument(help="the name of the label (title)")],
    color: Annotated[Colors, typer.Argument(help="the color to associate with the label")],
    is_json: Annotated[bool, typer.Option("--json", help="render output in JSON")] = False,
) -> None:
    """
    Define the labels available for a board.
    """
    label = client.post_label(board_id, name, color.value)
    if is_json:
        console.print_json(data=label)
        return
    render_label(label)


@app.command()
def add_label_to_card(
    card_id: Annotated[str, typer.Argument(help="the card id to attach label to")],
    label_id: Annotated[str, typer.Argument(help="a label id to associate with a card")],
    is_json: Annotated[bool, typer.Option("--json", help="render output in JSON")] = False,
) -> None:
    """
    Attach label to a card.
    """
    data = client.post_label_id_to_card(card_id, label_id)
    card = client.get_card_by_id(card_id)
    comments = client.get_comments_by_card_id(card_id)
    card["commentData"] = comments
    if is_json:
        console.print_json(data=card)
        return
    render_card(card)

if __name__ == "__main__":
    app()
