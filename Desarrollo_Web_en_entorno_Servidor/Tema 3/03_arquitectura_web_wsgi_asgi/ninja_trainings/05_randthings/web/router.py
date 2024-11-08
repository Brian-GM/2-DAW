from typing import Callable, Iterator
from controllers import home, random_number, sentence
from templates import render_template


def app(environ: dict, start_response: Callable) -> Iterator:
    """Aplicación de ejemplo.

    La versión más simple con respuesta en texto plano.

    :environ dict: diccionario que contiene las variables de entorno CGI así
                   como otros parámetros y metadatos.
    :start_response Callable: es una función ("Callable") que recibe dos
                              parámetros: el estado (status) y las cabeceras
                              de la respuesta (header response).

    :return: devuelve el cuerpo de la respuesta como un "Iterator" de bytes.
             Así, se devuelve el cuerpo como "byte" y no como "str".
    """
    path: str = environ.get("PATH_INFO")

    if path.endswith("/"):
        path = path[:-1]

    if path == "" or path == "/home":
        data: str = home(environ)

    elif path == "/random/number":
        data: str = random_number(environ)

    elif path == "/random/sentence":
        data: str = sentence(environ)
    else:
        data: str = render_template("views/404.html")

    data_in_bytes: bytes = data.encode("utf-8")

    start_response(
        "200 OK",
        [("Content-Type", "text/html"), ("Content-Length", str(len(data_in_bytes)))],
    )

    return iter([data_in_bytes])
