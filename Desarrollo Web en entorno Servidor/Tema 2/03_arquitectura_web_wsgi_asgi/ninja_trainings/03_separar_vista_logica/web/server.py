from typing import Callable, Iterator
from urllib.parse import parse_qs


def main(environ: dict, start_response: Callable) -> Iterator:
    qs_dict: dict[str, list[str]] = parse_qs(environ["QUERY_STRING"])
    lang: str = str(qs_dict["lang"][0])
    template_name: str = "views/spanish.html"

    if lang in qs_dict and qs_dict["lang"][0] == "en":
        template_name: str = "views/english.html"
        html_str = ""
        html_lang_list: str = "<ul><li>Python</li><li>Js</li><li>CSS</li></ul>"
        with open(template_name, "r", encoding="utf-8") as file_object:
            html_str = file_object.read()
        html_str = html_str.format(lang_list=html_lang_list)
        html_in_bytes: bytes = html_str.encode("utf-8")

    start_response("200 OK", [])
    return iter([html_in_bytes])
