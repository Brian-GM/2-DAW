def ask_and_add_pets(person: dict, count:int) -> None:
    print(f"Vamos a crear {count} mascotas")
    for _ in range(count) :
      name_pet: str = input("Escriba el nombre de la mascota: ")
      type_pet: str = input ("Escriba el tipo de mascota: ")
      pets: dict = {
        "name": "",
        "type": ""
      }
      pets["name"] = name_pet
      pets["type"] = type_pet
      person["pets"].append(pets)


def get_dog_name(info_people: list[dict]) -> str:
    dog_name_list: list[str] = []
    for owner in info_people:
        for pet in owner["pets"]:
            if pet["name"] == "Dog":
                dog_name_list.append(pet["name"])
    return dog_name_list