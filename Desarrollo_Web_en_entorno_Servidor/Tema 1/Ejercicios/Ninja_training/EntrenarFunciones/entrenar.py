
"""
Varias funciones para aprender python
"""
#El _ es el comodin de python


def hello_world() -> None:

    """
    Funcion hola mundo
    """
    print("Hola mundo")

hello_world()

for _ in range(1057):
    hello_world()


def from_name_to_list(name: str) -> list[str]:
    """
    Convierte un nombre a lista de caracteres.

    :name str: El nombre.

    :return: Lista de los caracteres del nombre.
    """

    lista: list[str] = []
    for c in name:
        lista.append(c)
    return lista


from_name_to_list('Roman')


def list_between_cuots(lista: list[int], high: int, low: int) -> list[int]:
    resultado: list[int] = []
    for n in lista:
        if n >= low and n <= high:
            resultado.append(n)

    return resultado


list_between_cuots([1,2,3,4,5,6,7,8,9], 8, 2)


def ask_for_people_info(num_of_persons: int) -> list[tuple[str, int]]:
    list_persons: list[tuple[str,int]] = []
    for n in range(num_of_persons):

        name: str = input("Name: ")
        age: int = int(input("Age: "))

        person: tuple[str,int] = (name,age)

        list_persons.append(person)

    return list_persons

ask_for_people_info(2)