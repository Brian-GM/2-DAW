"""
Funcion que coge una lista de diccionarios y suma sus edadesw devolviendo la media

"""
l: list[dict] = [
  {
    "name": "A",
    "age": "23",
    "lastname": "Aa"
  },
  {
    "name": "B",
    "age": "70",
    "lastname": "Bb"
  },
  {
    "name": "C",
    "age": "7",
    "lastname": "Cc"
  },
  {
    "name": "D",
    "age": "53",
    "lastname": "Dd"
  }
]


def age_avg(people: list[dict]) -> float:
    """
    SI
    """
    total_age: int = 0
    total_persons: int = 0
    for person in people:
        if "age" in person:
            total_age += person["age"]
            total_persons += 1
    return total_age/total_persons



age_avg(l)

from collections import namedtuple

Person = namedtuple ("Person",["name","age","lastname"])
person_list: list[Person] = [
    Person("a",22,"aa"),
    Person("b",40,"bb"),
    Person("c",80,"cc"),

]

def age_avg_person(people: list[Person]) -> float:
    total_age:int = 0
    for Person in people:
        total_age += Person.age
        return total_age / len(people)
    


age_avg_person(person_list)


def get_dog_name(info_people: list[dict]) -> str:
    dog_name_list: list[str] = []
    for owner in info_people:
        for pet in owner["pets"]:
            if pet["name"] == "Dog":
                dog_name_list.append(pet["name"])
    return dog_name_list
