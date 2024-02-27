from src.templates import render_template
from urllib.parse import parse_qs
from multipart import parse_form_data


def home() -> str:
    return render_template("src/views/index.html")


def form_contact(environ: dict[str, list[str]]) -> str:
    method: str = environ.get("REQUEST_METHOD", "").upper()
    context: dict[str, str] = {
		"username": "",
		"username_error": ""
	}

    if method == "GET":
        form: dict = parse_qs(environ["QUERY_STRING"])
        return validar(form)

    elif method == "POST":
        form: dict = parse_form_data(environ)
        return validar(form)


def validar(form: dict[str, str]):
    if "username" not in form:
        return render_template(
            "src/views/form_contact.html",
            context={"username": "", "username_error": ""},
        )

    # username: str = form["username"][0].strip()
    form["username"] = form["username"][0].strip()

    if form["username"] == "":
        return render_template(
            "src/views/form_contact.html",
            context={"username": "", "username_error": "No puede estar vacio"},
        )
    elif len(form["username"]) < 3:
        return render_template(
            "src/views/form_contact.html",
            context={"username": "", "username_error": "Ta chikito"},
        )

    return render_template(
        "src/views/message.html",
        context={"message": "Ta gud"},
    )


def error404() -> str:
    return render_template("src/views/404.html")
