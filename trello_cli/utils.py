from rich.console import Console, Group
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.columns import Columns
from rich.rule import Rule


console = Console()


def render_card(card_data: dict, render_output: bool = True) -> Panel:

    description_body = f"""
    [i]Description:[/i]
    {card_data.get("desc")}
    """

    comments = "\n".join([f"- {x['memberCreator']['fullName']}: {x['data']['text']}" for x in card_data.get("commentData")])

    comment_body = f"""
    [i]Comments:[/i]
    {comments}
    """

    labels = ", ".join(
        [f"[{x['color']}]{x['name']}[/{x['color']}]" for x in card_data.get("labels")]
    )

    label_body = f"""
    :label:  [i]Labels:[/i]
    {labels}
    """

    panel_group = Group(
        description_body,
        comment_body,
        label_body,
        fit=False,
    )
    panel = Panel(
        renderable=panel_group,
        expand=False,
        title="[b]" + card_data.get("name") + "[/b]",
        subtitle=card_data.get("id"),
        title_align="left",
        subtitle_align="right",
    )
    if render_output:
        console.print(panel)
    return panel


def render_cards(card_data: dict) -> None:
    column = Columns(column_first=True)
    for card in card_data:
        panel = render_card(card, False)
        column.add_renderable(panel)
    console.print(column)


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


def render_labels_list(labels_list_data: dict) -> None:
    table = Table(title="Trello labels")
    table.add_column("Label Name")
    table.add_column("color")
    table.add_column("Label ID")
    table.add_column("Board ID")
    for l in labels_list_data:
        table.add_row(
            l.get("name"),
            l.get("color"),
            l.get("id"),
            l.get("idBoard"),
        )
    console.print(table)


def render_label(label_data: dict) -> None:
    pass


def render_list(list_data: dict, render_output: bool = True) -> None:
    column = Columns(title=list_data.get("name"), column_first=True, expand=True)
    for card in list_data.get("cardData"):
        panel = render_card(card, False)
        column.add_renderable(panel)
    if not list_data.get("cardData"):
        column.add_renderable(Rule(title="No Cards"))
    if render_output:
        console.print(column)
    return column


def render_board(board_data: dict) -> None:
    layout = Layout(name="board")
    layout.split(
        Layout(name="header", size=1),
        Layout(name="body"),
    )
    layout["header"].update(
        Rule(title=board_data.get("name"))
    )
    columns = []
    for each in board_data.get("listData"):
        column = render_list(each, False)
        columns.append(column)
    layout["body"].split_row(*[Layout(column) for column in columns])
    console.print(layout)