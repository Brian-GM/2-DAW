from typing import Callable, Iterator
from http.cookies import SimpleCookie


def app(environ: dict, start_response: Callable) -> Iterator:
    data: str = "Hola mundo"
    data_in_bytes: bytes = data.encode("utf-8")
    if "HTTP_COOKIE" in environ:
        cookies: SimpleCookie = SimpleCookie()
        cookies.load(environ["HTTP_COOKIE"])
        if "name" in cookies:
            data: str = f"Hola {cookies['name'].value}"
    data_in_bytes: bytes = data.encode("utf-8")
    start_response("200 OK", {("Set-Cookie", "name=Brian")})
    return iter([data_in_bytes])
