# Trello CLI

Built with [Typer](https://typer.tiangolo.com/), [Pydantic](https://docs.pydantic.dev/latest/), and [Requests](https://requests.readthedocs.io/en/latest/).

Typer is a framework built on Click, a popular CLI library for Python.  It adds web framework style conventions and a clean, structured programming paradigm, leveraging decorator syntax to make CLI development more readily maintainable.

Pydantic brings type validation to Python, and helps to ensure objects are consistently marshalled.  We use it in this case for env settings management as well.

Requests is a popular library for managing network requests and responses.

## Documentation

For usage documentation please refer to [USAGE.md](USAGE.md)

API_KEY and API_TOKEN must be set through either env variables or a .env file in your execution directory.
the format of the .env file is as follows:

```
api_key="xxxxxxxx"
api_token="xxxxxxxxx"
```

## TODO

Next steps on this project would be to implement delete and update functionality for comments, archival and movement for cards, and to expand test coverage significantly.