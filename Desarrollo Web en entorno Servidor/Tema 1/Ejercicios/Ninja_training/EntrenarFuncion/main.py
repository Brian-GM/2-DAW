from func import ask_and_add_pets, get_dog_name


info_people = [
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
    },
    {
        "name": "c",
        "age": 35,
        "pets": []
    },
    {
        "name": "d",
        "age": 42,
        "pets": [
            {
                "name": "Buddy",
                "type": "Dog"
            },
            {
                "name": "Whiskers",
                "type": "Cat"
            }
        ]
    },
    {
        "name": "e",
        "age": 60,
        "pets": []
    },
    {
        "name": "f",
        "age": 22,
        "pets": [
            {
                "name": "Luna",
                "type": "Dog"
            },
            {
                "name": "Snowball",
                "type": "Cat"
            }
        ]
    },
    {
        "name": "g",
        "age": 45,
        "pets": [
            {
                "name": "Rocky",
                "type": "Dog"
            }
        ]
    }
]

ask_and_add_pets(info_people, 1)
