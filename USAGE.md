# `Trello-CLI`

A simple CLI for interacting with Trello Cards.

Current capabilities allow for:

    - Listing boards, lists, and cards

    - Viewing a board, list, or card

    - Adding a new list to a board

    - Adding a new card to a list / board

    - Commenting on a card

    - Adding labels to a card


No delete or move functionality has been implemented yet.

**Usage**:

```console
$ Trello-CLI [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `add-comment-to-card`: Attach label to a card.
* `add-label`: Define the labels available for a board.
* `add-label-to-card`: Attach label to a card.
* `create-card`: Create a new card on a Trello board.
* `get-board`: Fetch a Trello board by id.
* `get-boards`: Fetch all Trello boards for the...
* `get-card`: Fetch a card using the id field.
* `get-cards`: Fetch a card using the id field.
* `get-labels`: Fetch the labels for a given Trello board id.
* `get-list`: Fetch a Trello list by id.
* `get-lists`: Fetch the Trello lists for a given board id.

## `Trello-CLI add-comment-to-card`

Attach label to a card.

**Usage**:

```console
$ Trello-CLI add-comment-to-card [OPTIONS] CARD_ID COMMENT
```

**Arguments**:

* `CARD_ID`: the card id to attach label to  [required]
* `COMMENT`: a comment to attach to a card  [required]

**Options**:

* `--json`: render output in JSON
* `--help`: Show this message and exit.

## `Trello-CLI add-label`

Define the labels available for a board.

**Usage**:

```console
$ Trello-CLI add-label [OPTIONS] BOARD_ID NAME COLOR:{green|yellow|orange|red|purple|blue|sky|lime|pink|black}
```

**Arguments**:

* `BOARD_ID`: the board id to add the label to  [required]
* `NAME`: the name of the label (title)  [required]
* `COLOR:{green|yellow|orange|red|purple|blue|sky|lime|pink|black}`: the color to associate with the label  [required]

**Options**:

* `--json`: render output in JSON
* `--help`: Show this message and exit.

## `Trello-CLI add-label-to-card`

Attach label to a card.

**Usage**:

```console
$ Trello-CLI add-label-to-card [OPTIONS] CARD_ID LABEL_ID
```

**Arguments**:

* `CARD_ID`: the card id to attach label to  [required]
* `LABEL_ID`: a label id to associate with a card  [required]

**Options**:

* `--json`: render output in JSON
* `--help`: Show this message and exit.

## `Trello-CLI create-card`

Create a new card on a Trello board.

**Usage**:

```console
$ Trello-CLI create-card [OPTIONS] TITLE BODY LIST_ID
```

**Arguments**:

* `TITLE`: the title of the card  [required]
* `BODY`: a description for the card  [required]
* `LIST_ID`: the id of the list the card should be added to  [required]

**Options**:

* `--label-ids TEXT`: the board id to retrieve lists from
* `--json`: render output in JSON
* `--help`: Show this message and exit.

## `Trello-CLI get-board`

Fetch a Trello board by id.

**Usage**:

```console
$ Trello-CLI get-board [OPTIONS] BOARD_ID
```

**Arguments**:

* `BOARD_ID`: the board id  [required]

**Options**:

* `--json`: render output in JSON
* `--help`: Show this message and exit.

## `Trello-CLI get-boards`

Fetch all Trello boards for the authenticated user.

**Usage**:

```console
$ Trello-CLI get-boards [OPTIONS]
```

**Options**:

* `--json`: render output in JSON
* `--help`: Show this message and exit.

## `Trello-CLI get-card`

Fetch a card using the id field.

**Usage**:

```console
$ Trello-CLI get-card [OPTIONS] CARD_ID
```

**Arguments**:

* `CARD_ID`: the card id  [required]

**Options**:

* `--json`: render output in JSON
* `--help`: Show this message and exit.

## `Trello-CLI get-cards`

Fetch a card using the id field.

**Usage**:

```console
$ Trello-CLI get-cards [OPTIONS] BOARD_ID [LIST_ID]
```

**Arguments**:

* `BOARD_ID`: the board id to retrieve cards from  [required]
* `[LIST_ID]`: optionally provide list_id to filter results by list

**Options**:

* `--json`: render output in JSON
* `--help`: Show this message and exit.

## `Trello-CLI get-labels`

Fetch the labels for a given Trello board id.

**Usage**:

```console
$ Trello-CLI get-labels [OPTIONS] BOARD_ID
```

**Arguments**:

* `BOARD_ID`: the board id to retrieve labels for  [required]

**Options**:

* `--json`: render output in JSON
* `--help`: Show this message and exit.

## `Trello-CLI get-list`

Fetch a Trello list by id.

**Usage**:

```console
$ Trello-CLI get-list [OPTIONS] LIST_ID
```

**Arguments**:

* `LIST_ID`: the list id  [required]

**Options**:

* `--json`: render output in JSON
* `--help`: Show this message and exit.

## `Trello-CLI get-lists`

Fetch the Trello lists for a given board id.

**Usage**:

```console
$ Trello-CLI get-lists [OPTIONS] BOARD_ID
```

**Arguments**:

* `BOARD_ID`: the board id to retrieve lists from  [required]

**Options**:

* `--json`: render output in JSON
* `--help`: Show this message and exit.
