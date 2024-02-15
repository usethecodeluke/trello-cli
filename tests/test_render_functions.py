from trello_cli.utils import *
from .test_data import test_data


card_data  = test_data["listData"][0]["cardData"][0]
list_data  = test_data["listData"][0]
list_data2  = test_data["listData"][-1]


def test_render_card(card_data: dict = card_data) -> None:
    panel = render_card(card_data, False)
    assert type(panel.renderable) == Group
    assert len(panel.renderable.renderables) == 3
    assert panel.title == "[b]Card Number 2[/b]"


def test_render_list_with_cards(list_data: dict = list_data) -> None:
    column = render_list(list_data, False)
    assert type(column.renderables) == list
    assert len(column.renderables) == 2
    assert type(column.renderables[0]) == Panel
    assert column.title == "To Do"


def test_render_list_without_cards(list_data: dict = list_data2) -> None:
    column = render_list(list_data, False)
    assert len(column.renderables) == 1
    assert type(column.renderables[0]) == Rule
    assert column.title == "Done"
