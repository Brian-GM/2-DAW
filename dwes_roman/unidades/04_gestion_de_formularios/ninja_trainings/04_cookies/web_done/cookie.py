from typing import Callable, Iterator
from http.cookies import SimpleCookie
from src.controllers import home, yourname, error404
from urllib.parse import quote,unquote


def app(environ: dict, start_response: Callable) -> Iterator:
    path: str = environ.get("PATH_INFO")
    headers: list[tuple[str, str]] = [
        ("Content-Type", "text/html")
    ]

    if path.endswith("/"):
        path = path[:-1]

    if path == "" or path == "/home":
        data: str = home(environ)
    elif path == "/yourname":
        data: str = yourname(environ, headers) #Crea cookie en yourname
    else:
        data: str = error404()

    data_in_bytes: bytes = data.encode("utf-8")
    headers.append(("Content-Length", str(len(data_in_bytes))))
    start_response("200 OK", headers)

    return iter([data_in_bytes])

#!Mandar cookies
def mandar(environ: dict[str, list[str]], headers: list[tuple[str, str]]) -> str:
    cookiecifrada: str = quote("Pédro")
    headers.append(("Set-Cookie", f"name={cookiecifrada}"))

    return render_template("src/views/message.html", {"message": "Gracias ;)"})


#!Coger cookie
def coger(environ: dict[str, list[str]]):
    cookies: SimpleCookie = SimpleCookie()
    if "HTTP_COOKIE" in environ:
        cookies.load(environ["HTTP_COOKIE"])
    
    if "name" in cookies:
        nameencode: str = cookies["name"].value
        name: str = unquote(nameencode)
        print(name)
    


