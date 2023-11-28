from typing import Callable, Iterator
from urllib.parse import parse_qs


def app(environ: dict, start_response: Callable) -> Iterator:
    # Parseamos el "query parameter"
    qs_dict: dict[str, list[str]] = parse_qs(environ["QUERY_STRING"])

    if "name" in qs_dict:
        name: str = qs_dict["name"][0]

        data: str = f"""
    <!DOCTYPE html>
        <html>
            <head>
                <title>Mi e</title>
                <meta charset="utf-8">
            </head>
            <body>
                <h1>Hola {name} </h1>
            </body>
        </html>
                """

        # Convertidos a bytes
        data_in_bytes: bytes = data.encode("utf-8")

        start_response(
            "200 OK",
            [
                ("Content-Type", "text/html"),
                ("Content-Length", str(len(data_in_bytes))),
            ],
        )
    else:
        data: str = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Mi e</title>
                <meta charset="utf-8">
            </head>
            <body>
                <h1>BAD REQUEST </h1>
            </body>
        </html>
                    """

        # Convertidos a bytes
        data_in_bytes: bytes = data.encode("utf-8")

        start_response(
            "401 BAD REQUEST",
            [
                ("Content-Type", "text/html"),
                ("Content-Length", str(len(data_in_bytes))),
            ],
        )
    return iter([data_in_bytes])
