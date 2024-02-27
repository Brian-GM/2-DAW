from urllib.parse import parse_qs

from multipart import parse_form_data

from src.templates import render_template


def home() -> str:
    return render_template("src/views/index.html")


def form_username(environ: dict[str, list[str]]) -> str:
    # Método por el que nos han enviado el formulario.
    method: str = environ.get("REQUEST_METHOD", "").upper()

    # Dependiendo del método se tiene que procesar de una manera u otra.
    if method == "GET":
        # Obtenemos el query string y lo transformamos en un dict[str, str].
        qs: dict[str, list[str]] = parse_qs(
            environ["QUERY_STRING"],
            keep_blank_values=True
        )
        form: dict[str, str] = {key: value[0] for key, value in qs.items()}
        return compute_form(form)
    elif method == "POST":
        # Obtenemos el formulario (y los ficheros que vamos a ignorar) por
        # medio de la biblioteca multipart de Python.
        form, files = parse_form_data(environ)
        return compute_form(form)
    else:
        return render_template("src/views/404.html")


def compute_form(form: dict[str, str]) -> str:
    # Si no está el campo "username" es porque no se ha enviado el formulario.
    # Dicho de otro modo: es la primera vez que se carga el formulario.
    # Así que lo enviamos vacío, por primera vez.
    if "username" not in form:
        return render_template(
            "src/views/form_username.html",
            {
                "username": "",
                "username_error": "",
            }
        )

    errors: int = 0

    # Limpiamos y validamos los campos (solo hay uno).
    # 1. Quitamos espacios extras delante y detrás.
    form["username"] = form["username"].strip()

    # 2. comprobar que no esté vacío y que no tenga espacios.
    if not form["username"]:
        form["username_error"] = "Campo obligatorio"
        errors += 1
    elif " " in form["username"]:
        form["username_error"] = "El nombre de usuario no puede tener espacios"
        errors += 1
    else:
        form["username_error"] = ""

    if errors == 0:
        # Si no hay errores => se ha enviado el formulario correctamente.
        return render_template(
            "src/views/message.html",
            {"message": f"Nombre de usuario que has escrito: {form['username']}"}
        )
    else:
        # Si hay errores => volvemos al formulario pasándole los valores.
        return render_template("src/views/form_username.html", form)


def error404() -> str:
    return render_template("src/views/404.html")
