"""
Funcion que coge una lista de diccionarios y suma sus edadesw devolviendo la media

"""
from collections import namedtuple
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


Person = namedtuple("Person", ["name", "age", "lastname"])
person_list: list[Person] = [
    Person("a", 22, "aa"),
    Person("b", 40, "bb"),
    Person("c", 80, "cc"),

]


def age_avg_person(people: list[Person]) -> float:
    total_age: int = 0
    for Person in people:
        total_age += Person.age
        return total_age / len(people)


age_avg_person(person_list)


info_people: list[dict] = [
    {
        "name": "a",
        "age": 28,
        "pets": [

            {
                "name": "Otto",
                "type": "Dog"
            },
            {
                "name": "Pedro",
                "type": "Dog"
            },
        ]
    },
    {
        "name": "b",
        "age": 50,
        "pets": [

            {
                "name": "Mishi",
                "type": "Cat"
            },
            {
                "name": "Fu",
                "type": "Cat"
            }
        ]
    }
]


def get_dog_name(info_people: list[dict]) -> str:
    dog_name_list: list[str] = []
    for owner in info_people:
        for pet in owner["pets"]:
            if pet["name"] == "Dog":
                dog_name_list.append(pet["name"])
    return dog_name_list


def ask_and_add_pets(person: dict, count: int) -> None:
    print(f"Vamos a crear {count} mascotas")
    for _ in range(count):
        name_pet: str = input("Escriba el nombre de la mascota: ")
        type_pet: str = input("Escriba el tipo de mascota: ")
        pets: dict = {
            "name": "",
            "type": ""
        }
        pets["name"] = name_pet
        pets["type"] = type_pet
        person["pets"].append(pets)


ask_and_add_pets(info_people[1], 2)


print(info_people)
