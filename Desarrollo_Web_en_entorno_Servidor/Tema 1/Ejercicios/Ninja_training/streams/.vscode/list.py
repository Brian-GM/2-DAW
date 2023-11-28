"""
Lis y dict comprension
"""

from random import randint


def multiply_odd_by_two(numbers: list[int]) -> list[int]:
    numbers: list[int] = [n * 2 for n in numbers if n % 2 != 0]
    return numbers


#!dict comprension


def list_to_dictionary(people: list[str]) -> dict[str]:
    people_numbers: dict[str, int] = {}
    for person in people:
        people_numbers[person] = randint(1, 100)
    return people_numbers


def list_to_dictionary_comprension(people: list[str]) -> dict[str]:
    people_numbers: dict[str, int] = {name: randint(1, 100) for name in people}
    return people_numbers


def pass_students(students: dict[str, int]) -> dict[str, int]:
    all_pass_students: dict[str, int] = {
        student for student, mark in students.items() if mark >= 5
    }
    return all_pass_students


# Metodo de roman
def pass_students_roman(students: dict[str, int]) -> dict[str, int]:
    students_pass: dict[str, int] = {
        name: mark for name, mark in students.item() if mark >= 5
    }


if __name__ == "__main__":
    ejem_numbers1: list[int] = [1, 2, 3, 4, 5]
    ejem_number2: list[int] = [3, 4, 8, 9, 1]
    ejem_text: list[str] = ["Ola", "Juan", "awanabumwawnawaw", "aaaaaaaaaaaaaaaaaa"]
    ejem_people: list[str] = ["Alice", "Juan", "Paco", "Joan"]
    ejem_students: dict[str, int] = {"Alice": 6, "Luis": 3, "Juen": 8, "Pedro": 10}

    # multiply_odd_by_two(ejem_numbers1)
    # list_to_dictionary(ejem_people)
    # list_to_dictionary_comprension(ejem_people)
    pass_students(ejem_students)
