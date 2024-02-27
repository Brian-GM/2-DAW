from src.templates import render_template
from multipart import parse_form_data
from urllib.parse import parse_qs



def home() -> str:
    return render_template("src/views/index.html")


def error404() -> str:
    return render_template("src/views/404.html")


def form_username(environ: dict[str, list[str]]) -> str:
    method: str = environ.get("REQUEST_METHOD", "").upper()
    if method == "GET":
        data: str = render_template("src/views/form_username.html")
        return data
    elif method == "POST":
        form, files = parse_form_data(environ)

        pass
    else:
        return error404()
    return "Está por hacer"
