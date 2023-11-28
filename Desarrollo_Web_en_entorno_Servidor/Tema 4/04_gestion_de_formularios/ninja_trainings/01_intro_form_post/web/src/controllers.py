from src.templates import render_template
from urllib.parse import parse_qs
from src.validator import is_username, is_password
from multipart import parse_form_data



def home() -> str:
    return render_template("src/views/index.html")


def error404() -> str:
    return render_template("src/views/404.html")


def form_sum(environ: dict[str, list[str]]) -> str:
    request_method: str = environ.get("REQUEST_METHOD", "GET").upper()
    forms, _ = parse_form_data(environ)
    for form_name,form_value in forms.items():
    number1: int = str()
    number2: int = str()
    valid_num1: bool = True
    valid_num2: bool = True
    if request_method == "POST":
        context: dict[str, str] = {
            "num1": "",
            "num2": "",
            "num_error": "",
        }
        return render_template("src/views/form_sum.html", context)
