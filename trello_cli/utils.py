from rich.console import Console, Group
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule


console = Console()


def render_card(card_data: dict) -> None:

    description_body = f"""
    [b]Description:[/b]
    {card_data.get("desc")}
    """

    labels = ", ".join(
        [f"[{x['color']}]{x['name']}[/{x['color']}]" for x in card_data.get("labels")]
    )

    label_body = f"""
    :label:  [b]Labels:[/b]
    {labels}
    """

    rule = Rule()

    panel_group = Group(
        description_body,
        rule,
        label_body,
    )
    panel = Panel(
        renderable=panel_group,
        expand=False,
        title=card_data.get("name"),
        title_align="left",
    )
    console.print(panel)


def render_board_list(board_list_data: dict) -> None:
    table = Table(title="Trello Boards")
    table.add_column("Board Name")
    table.add_column("Board ID")
    table.add_column("Last Modified")
    table.add_column("Starred")
    for board in board_list_data:
        table.add_row(
            board.get("name"),
            board.get("id"),
            board.get("dateLastActivity"),
            ":star:" if board.get("starred") else ":x:"
        )
    console.print(table)


def render_lists_list(lists_list_data: dict) -> None:
    table = Table(title="Trello Lists")
    table.add_column("List Name")
    table.add_column("List ID")
    table.add_column("Board ID")
    for l in lists_list_data:
        table.add_row(
            l.get("name"),
            l.get("id"),
            l.get("idBoard"),
        )
    console.print(table)


def render_board(board_data: dict) -> None:
    pass


def render_list(list_data: dict) -> None:
    pass