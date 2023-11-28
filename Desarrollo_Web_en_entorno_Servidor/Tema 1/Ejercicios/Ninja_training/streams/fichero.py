# * Para elevar  numero ** number
# ? Nombres en funciones lambda cortos solo una letra


def square_numbers(numbers: list[int]) -> list:
    result: list[int] = []
    for number in numbers:
        result.append = number**2
    return result


def square_numbers_map(numbers: list[int]) -> list:
    return list(map(lambda n: n**2, numbers))


def initials(text: list[str]) -> list[str]:
    inits: list[str] = []
    for word in text:
        inits.append(word[0])


def initials_map(text: list[str]) -> list[str]:
    return list(map(lambda t: t[0], text))


def lengths(text: list[str]) -> list[int]:
    return list(map(lambda t: len(t), text))


def listas(l1: list[int], l2: list[int]) -> list[int]:
    return list(map(lambda ln1, ln2: ln1 * ln2, l1, l2))


def par(l1: list[int]) -> list[int]:
    result: list[int] = []
    for n in l1:
        if n % 2 == 0:
            result.append(n)
    return result


def par_filter(l1: list[int]) -> list[int]:
    return list(filter(lambda ln1: ln1 % 2 == 0, l1))


def valid_password(text: list[str]) -> list[str]:
    return list(filter(lambda t: len(t) >= 8, text))


def words_with_upper_case(text: list[str]) -> list[str]:
    return list(filter(has_upper_case, text))


def has_upper_case(text: str) -> bool:
    for letter in text:
        if letter.isupper():
            return True
    return False




if __name__ == "__main__":
    ejem: list[int] = [1, 2, 3, 4, 5]
    ejem1: list[int] = [3, 4, 8, 9, 1]
    ejem2: list[str] = ["Ola", "Juan", "awanabumwawnawaw", "aaaaaaaaaaaaaaaaaa"]

# square_numbers(ejem)
# lengths(ejem2)
# listas(ejem,ejem1)
# par_filter(ejem)
# valid_password(ejem2)
print(words_with_upper_case(ejem2))
