from templates import render_template
from random import randint
from urllib.parse import parse_qs


# ?Renderiza el home
def home(environ: dict) -> str:
    return render_template("views/home.html")


def random_number(environ: dict) -> str:
    qs_dict: dict[str, str] = parse_qs(environ["QUERY_STRING"])
    random: int = 0
    number_min: int = 1
    number_max: int = 1_000_000

    if "from" in qs_dict and qs_dict["from"][0].isalnum:
        number_min = int(qs_dict["from"][0])

    if "to" in qs_dict and qs_dict["to"][0].isalnum:
        number_max = int(qs_dict["to"][0])

    random = randint(number_min, number_max)
    context: dict[str, str] = {"number": random}
    return render_template("views/number.html", context)


def sentence(environ: dict) -> str:
    with open("assets/sentences.txt", "r", encoding="utf8") as fd:
        sentences: list[str] = [line.rstrip("\n") for line in fd]
        random_sentence: str = sentences[randint(0, len(sentences) - 1)]
    context: dict[str, str] = {"sentence": random_sentence}
    return render_template("views/sentence.html", context)
