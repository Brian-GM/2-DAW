from models.data import DOGS
from classes.dog import Chihuahua, Labrador, Dog

"""
En el diccionario `models/data.py` tienes un diccionario donde se describen
labradores y chihuahuas (perros).

Lleva a cabo los pasos que se indican en los comentarios que hay debajo.

PD/ Tendrás que importar todo lo que sea necesario.
"""

# TODO Crear una lista de objetos Labrador a partir de los datos que ves en
#      la lista DOGS que hay en models/data.py.
labrador_list: list[Labrador] = [
    Labrador(dog["name"], dog["age"]) for dog in (DOGS["labrador"])
]
print(labrador_list)


# TODO Crear una lista de objetos Chihuahua a partir de los datos que ves en
#      la lista DOGS que hay en models/data.py.
chihuahua_list: list[Labrador] = [
    Chihuahua(dog["name"], dog["age"]) for dog in (DOGS["chihuahua"])
]
print(chihuahua_list)


# TODO Imprime por pantalla las descripciones de los labradores y de los
#      chihuahuas llamado al método `description`.
for dog in labrador_list:
    dog.description()
for dog in chihuahua_list:
    dog.description()

# TODO Imprime por pantalla los sonidos de los labradores y de los chihuahuas
#      pasándole el valor de 3 al parámetro `times` del método `sound`.
for dog in labrador_list:
    dog.sound(3)
for dog in chihuahua_list:
    dog.sound(3)
