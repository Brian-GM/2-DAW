from typing import Callable, Iterator
from urllib.parse import parse_qs


def main(environ: dict, start_response: Callable) -> Iterator:
    print(environ)
    qs_dict: dict[str, list[str]] = parse_qs(environ["QUERY_STRING"])
    html_str = ""
    context: dict[str, str] = {
        "lang_list": "<ul><li>Python</li><li>Js</li><li>CSS</li></ul>"
    }
    template_name: str = "views/spanish.html"

    if "lang" in qs_dict and qs_dict["lang"][0] == "en":
        template_name: str = "views/english.html"
    with open(template_name, "r", encoding="utf-8") as file_object:
        html_str = file_object.read()
    html_str = html_str.format(**context)
    html_in_bytes: bytes = html_str.encode("utf-8")

    start_response("200 OK", [])
    return iter([html_in_bytes])
