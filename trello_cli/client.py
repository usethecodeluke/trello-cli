import sys
import json

import typer
from requests import get, post, HTTPError
from rich import print


class TrelloClient:
    def __init__(
        self, api_key: str, api_token: str, api_url: str, workspace: str = None
    ):
        self.api_key = api_key
        self.api_token = api_token
        self.api_url = api_url
        self.workspace = workspace

    def get_boards(self) -> dict:
        result = self.execute_get(url=f"{self.api_url}/members/me/boards")
        return result

    def get_board_by_id(self, board_id: str) -> dict:
        result = self.execute_get(url=f"{self.api_url}/board/{board_id}")
        return result

    def get_lists_by_board_id(self, board_id: str) -> dict:
        result = self.execute_get(url=f"{self.api_url}/board/{board_id}/lists")
        return result

    def get_list_by_id(self, list_id: str) -> dict:
        result = self.execute_get(url=f"{self.api_url}/lists/{list_id}")
        return result

    def get_cards_by_board_id(self, board_id: str) -> dict:
        result = self.execute_get(url=f"{self.api_url}/boards/{board_id}/cards")
        return result

    def get_cards_by_list_id(self, list_id: str) -> dict:
        result = self.execute_get(url=f"{self.api_url}/lists/{list_id}/cards")
        return result

    def get_card_by_id(self, card_id: str) -> dict:
        result = self.execute_get(url=f"{self.api_url}/cards/{card_id}")
        return result

    def get_comments_by_card_id(self, card_id: str) -> dict:
        params = {"filter": "commentCard,copyCommentCard"}
        result = self.execute_get(
            url=f"{self.api_url}/cards/{card_id}/actions", params=params
        )
        return result

    def get_comments_by_list_id(self, list_id: str) -> dict:
        params = {"filter": "commentCard,copyCommentCard"}
        result = self.execute_get(
            url=f"{self.api_url}/lists/{list_id}/actions", params=params
        )
        return result

    def get_comments_by_board_id(self, board_id: str) -> dict:
        params = {"filter": "commentCard,copyCommentCard"}
        result = self.execute_get(
            url=f"{self.api_url}/boards/{board_id}/actions", params=params
        )
        return result

    def get_labels_by_board_id(self, board_id: str) -> dict:
        result = self.execute_get(url=f"{self.api_url}/boards/{board_id}/labels")
        return result

    def post_card(self, name: str, body: dict, list_id: str, label_ids: list) -> dict:
        labels = ",".join([id for id in label_ids])
        data = {
            "name": name,
            "idList": list_id,
            "desc": body,
            "idLabels": labels,
        }
        result = self.execute_post(url=f"{self.api_url}/cards", data=data)
        return result

    def post_label(self, board_id: str, name: str, color: str) -> dict:
        data = {"name": name, "idBoard": board_id, "color": color}
        result = self.execute_post(url=f"{self.api_url}/labels", data=data)
        return result

    def post_label_to_card(self, card_id: str, name: str, color: str) -> dict:
        data = {"name": name, "color": color}
        result = self.execute_post(
            url=f"{self.api_url}/cards/{card_id}/labels", data=data
        )
        return result

    def post_label_id_to_card(self, card_id: str, label_id: str) -> dict:
        data = {"value": label_id}
        result = self.execute_post(
            url=f"{self.api_url}/cards/{card_id}/idLabels", data=data
        )
        return result

    def post_comment_to_card(self, card_id: str, comment: str) -> dict:
        data = {"text": comment}
        result = self.execute_post(
            url=f"{self.api_url}/cards/{card_id}/actions/comments", data=data
        )
        return result

    def execute_get(
        self,
        url: str,
        headers: dict = None,
        params: dict = None,
    ):
        """
        Execute GET calls to the API.
        Optionally set custom headers and query params.
        """

        if headers is None:
            headers = {}
        headers["Accept"] = "application/json"

        if params is None:
            params = {}
        params["key"] = self.api_key
        params["token"] = self.api_token

        try:
            res = get(
                url,
                params=params,
                headers=headers,
            )
            res.raise_for_status()
            val = res.json()
        except HTTPError as exc:
            print(str(exc))
            sys.exit(1)
        return val

    def execute_post(
        self,
        url: str,
        headers: dict = None,
        params: dict = None,
        data: dict = None,
    ):
        """
        Execute POST calls to the API.
        Set body, and optionally set custom headers and query params.
        """

        if headers is None:
            headers = {}
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"

        if params is None:
            params = {}
        params["key"] = self.api_key
        params["token"] = self.api_token

        try:
            res = post(
                url,
                params=params,
                headers=headers,
                data=json.dumps(data),
            )
            res.raise_for_status()
            val = res.json()
        except HTTPError as exc:
            print(str(exc))
            sys.exit(1)
        return val
