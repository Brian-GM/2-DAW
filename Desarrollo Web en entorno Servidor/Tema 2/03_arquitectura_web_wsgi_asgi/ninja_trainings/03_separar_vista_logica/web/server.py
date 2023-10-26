from typing import Callable, Iterator


def main(environ: dict, start_response: Callable) -> Iterator:
    html_str = ""

    html_in_bytes: bytes = html_str.encode("utf-8")

    start_response("200 OK", [])
    return iter([html_in_bytes])
