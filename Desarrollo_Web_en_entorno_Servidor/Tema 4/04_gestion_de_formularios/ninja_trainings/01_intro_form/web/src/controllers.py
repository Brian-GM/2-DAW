from src.templates import render_template
from urllib.parse import parse_qs
from src.validator import is_username, is_password


def home() -> str:
    return render_template("src/views/index.html")


def error404() -> str:
    return render_template("src/views/404.html")


def form_username(environ: dict[str, list[str]]) -> str:
    username: str = ""
    password: str = ""
    valid_username: bool = True
    valid_password: bool = True

    qs: dict[str, list[str]] = parse_qs(environ["QUERY_STRING"])
    context: dict[str, str] = {
        "username": "",
        "username_error": "",
        "password": "",
        "password_error": "",
    }
    if "username" not in qs or "password" not in qs:
        return render_template("src/views/form_username.html", context)
    else:
        username = qs["username"][0]
        password = qs["password"][0]

        if is_username(username) == False:
            context[
                "username_error"
            ] = "No se permiten espacios en blanco en el username"
            valid_username = False

        if is_password(password) == False:
            context[
                "password_error"
            ] = "La contraseña debe tener minimo 8 caracteres y contener letras y numeros"
            valid_password = False

        if valid_username == True and valid_password == True:
            context["message"] = "Formulario enviado"
            return render_template("src/views/message.html", context)
        else:
            return render_template("src/views/form_username.html", context)
