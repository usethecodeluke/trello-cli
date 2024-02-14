from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Set the configuration paramameter types and defaults here.
    These can be overriden by dotenv files and parameters passed
    in at execution time.
    """

    api_host: str = "api.trello.com"
    api_version: int = 1
    api_key: str = ""
    api_token: str = ""
    board_name: str = "default"

    @property
    def api_url(self):
        url = f"https://{self.api_host}/{self.api_version}"
        return url


# We need the get_config function before everything else, so that we can pull
# environment variables and establish client connections. So assign it to cached
# result function and import from wherever needed.


@lru_cache()
def get_config():
    return Settings(_env_file=".env")
