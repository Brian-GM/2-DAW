from src.model.rick_and_morty.definitions import RICK_AND_MORTY_NAME, RICK_AND_MORTY_ORIGIN
from src.model.rick_and_morty.character import CHARACTER



def show(option: str) -> list:
    lista:list[str] = []
    if option == RICK_AND_MORTY_NAME:
        for character in CHARACTER["results"]:
            lista.append(character["name"])
        for name in lista:
            print(name)
        return lista

    elif option == RICK_AND_MORTY_ORIGIN:
        for character in CHARACTER["results"]:
            lista.append(character["origin"]["name"])
        for origin_name in lista:
            print(origin_name)
        return lista

    else:
        return[]

    