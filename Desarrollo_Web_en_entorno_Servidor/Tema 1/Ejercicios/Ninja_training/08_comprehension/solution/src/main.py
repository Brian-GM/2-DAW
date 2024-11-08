"""List/Dict Comprehension.

A continuación tienes una lista de ejercicios propuestos para que practiques
con una de las herramientas más utilizadas en Pytho: comprehensions.

Ejecuta los tests para comprobar que lo has hecho bien (o, por lo menos, que
los tests han pasado, que no es poco :P)
"""
from random import randint


# TODO Escribe una función llamada `initials` que dada una lista de strings
#      devuelva la lista de las iniciales en mayúsculas.
def initials(strings: list[str]) -> list[str]:
    return [i[0].upper() for i in strings]


# TODO Escribe una función llamada `even_numbers` que reciba un rango de
#      números y devuelva una lista con los números pares que hay en ese
#      rango.
def even_numbers(n1: int, n2: int) -> list[int]:
    return [n for n in range(n1, n2 + 1) if n % 2 == 0]


# TODO Escribe una función llamada `only_letters` que reciba un string y
#      devuelva la lista de las letras de esa cadena. Solo las letras, nada de
#      comas, puntos, números, etc.
#
#      Ayuda: en Python existen multitud de métodos para strings. Seguro que
#      existe algún método que dado un carácter te diga si dicho caracter es
#      letra o no.
def only_letters(string: str) -> list[str]:
    return [char for char in string if char.isalpha()]


# TODO Escribe una función llamada `random_number` que reciba una lista de
#      nombres de personas y asigne un número al azar entre 1 y 10a cada uno
#      de ellos, devolviendo un diccionario con esta información.
#
#      Por ejemplo, dado este listado de nombres:
#      ["Alice", "Bob", "Mary", "Jon"]
#
#      Dolvería algo así:
#      {"Alice": 3, "Bob": 5, "Mary": 1, "Jon": 7}
def random_number(people: list[str]) -> dict[str, int]:
    return {name: randint(1, 10) for name in people}


# TODO Escribe una función llamada `assign_numbers` que reciba una lista de
#      nombres de persona y asigne un número incremental a cada uno de ellos
#      de 1 en adelante, generando un diccionario que devolverá como
#      resultado.
#
#     Por ejemplo, dado este listado de nombres:
#     ["Alice", "Bob", "Mary", "Jon"]
#
#     Dolvería algo así:
#     {"Alice": 1, "Bob": 2, "Mary": 3, "Jon": 4}
def assign_numbers(people: list[str]) -> dict[str, int]:
    return {name: i + 1 for i, name in enumerate(people)}


# TODO Escribe una función `accum_game` que devuelva la suma de las
#      puntuaciones de un juego.
#      
#      Esta función recibirá un diccionario como este:
#      {"Alice": 77, "Bob": 85, "Mary": 37, "Jon": 45}
#
#      En este caso, devolvería 244, que es la suma de 77 + 85 + 37 + 45.
def accum_game(info: dict[str, int]) -> int:
    return sum([points for name, points in info.items()])


# TODO En Python tenemos una función muy utilizada llamada `zip`. En este
#      ejercicio vas a tener que investigar cómo usar dicha función.
#
#      Escribe una función llamada `grades` que dadas dos listas devuelva un
#      diccionario con la información de los estudiantes y sus notas. La 
#      primera lista contendrá el nombre de los estudiantes y la segunda sus
#      notas. Ambas listas tendrán el mismo número de elementos.
#
#      Por ejemplo, si recibe estas dos listas:
#      names: ["Alice", "Bob", "Mary", "Jon"]
#      marks: [7.5, 8.0, 3.75, 10]
#
#      Devolvería este diccionario:
#      {"Alice": 7.5, "Bob": 8.0, "Mary": 3.75, "Jon": 10}
def grades(names: list[str], marks: list[float]) -> dict[str, float]:
    return {name: mark for name, mark in zip(names, marks)}


# TODO Escribe una función llamada `grades_for_pass_students` que haga lo 
#      mismo que la función anterior pero que devuelva solo el diccionario de
#      los estudiantes que han aprobado.
def grades_for_pass_students(
    names: list[str], marks: list[float]
) -> dict[str, float]:
    return {name: mark for name, mark in zip(names, marks) if mark >= 5}
