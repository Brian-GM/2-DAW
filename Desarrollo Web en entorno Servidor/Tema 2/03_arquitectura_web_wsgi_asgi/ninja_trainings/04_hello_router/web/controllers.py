from templates import render_template

# , get_menu


def home(environ: dict) -> str:
    context: dict[str, str] = {"menu": render_template("views/menu.html")}
    return render_template("views/home.html", context)


def python(environ: dict) -> str:
    context: dict[str, str] = {"menu": render_template("views/menu.html")}
    return render_template("views/python.html", context)


def java(environ: dict) -> str:
    context: dict[str, str] = {"menu": render_template("views/menu.html")}
    return render_template("views/java.html", context)


def php(environ: dict) -> str:
    context: dict[str, str] = {"menu": render_template("views/menu.html")}
    return render_template("views/php.html", context)
