import typer

from requests import get, post, RequestException
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

    def get_card(self, card_id: str) -> dict:
        result = self.execute_get(url=f"{self.api_url}/cards/{card_id}")
        return result

    def post_card(self, title: str, body: dict, headers: dict, params: dict) -> dict:
        pass

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
        except RequestException as exc:
            print(exc.strerror)
            typer.Abort(code=1)

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
                data=data,
            )
            res.raise_for_status()
            val = res.json()
        except RequestException as exc:
            print(exc.strerror)
            typer.Abort(code=1)

        return val
