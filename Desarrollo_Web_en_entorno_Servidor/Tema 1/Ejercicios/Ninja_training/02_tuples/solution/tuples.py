"""Tuplas y namedtuples.

Completa el código fuente que tienes debajo. Hay comentarios TODO que indican
lo que tienes que hacer justo en esa posición.

Cuando completes el código puedes ejecutar los tests con `pytest` desde el
directorio raíz para comprobar si está bien.
"""

from collections import namedtuple


vowels = ("a", "e", "i", "o", "u")
upper_vowels = ("A", "E", "I", "O", "U")

# TODO cambia el valor de la siguiente variable para que contenga la cuarta
#      vocal de `vowels`.
forth_vowel: str | None = vowels[3]

# TODO cambia el valor de la variable siguiente para que sea una tupla con los
#      elementos de `vowels` y `upper_vowels`.
all_vowels: tuple[str] | None = vowels + upper_vowels

# TODO cambia el valor de la siguinete variable para que sea una tupla que
#      conste del valor True 100 veces.
too_true: tuple[bool] | None = (True,) * 100

# TODO comprueba si existe el valor `False` en `too_true` con el operador `in`
#      y guarda el resultado de la comprobación en la siguiente variable.
has_false: bool | None = False in too_true

# TODO crea un nuevo namedtuple (tipo) llamado `Location` que contenga tres
#      atributos llamados: `lat`, `lon`, `altitude`, `distance`.
Location = namedtuple("Location", ["lat", "lon", "altitude", "distance"])  # cambia este None por la declaracion del namedtuple

# TODO crea una lista con tres localizaciones (invéntate los valores. Los 4
#      atributos son valores enteros).
locations: list[Location] | None = [
    Location(1, 1, 1, 1),
    Location(2, 2, 2, 2),
    Location(3, 3, 3, 3),
    Location(4, 4, 4, 4)
]

# TODO asigna a la siguinete variable la `altitude` del tercer `Location` de la
#      lista locations.
altitude: int | None = locations[2].altitude
