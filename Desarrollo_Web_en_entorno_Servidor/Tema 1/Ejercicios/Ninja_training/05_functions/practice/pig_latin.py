"""Pig Latin.

Pig Latin es un juego lingüístico en el que palabras, en inglés, son alteradas,
normalmente añadiendo un sufijo fabricado o moviendo letras de la palabra al
final. Por ejemplo: la palabra "Wikipedia" se transforma en "Ikipediaway"
(cogiendo la "W", moviéndola al final y añadiendo el sufijo "ay").

Si quieres saber más puedes echar un vistazo a la Wikipedia:
https://en.wikipedia.org/wiki/Pig_Latin

El Pig Latin es usado como forma de diversión hoy en día, y también es usado
por gente joven cuando quiere ocultar sus conversaciones delante de gente
mayor. Por ejemplo, dos personas jóvenes podrían estar hablando y decirse el
uno al otro: "ehay isay eryvay illysay" lo que significa "he is very silly".

Dejando a un lado las anécdotas sobre el Pig Latin, en este fichero tienes que
escribir una función llamada `pig_lagin` que reciba un string con una frase en
inglés y devuelva la frase convertida a Pig Latin. La frase puede contener, por
tanto, una o más palabras.

Puedes usar todas las funciones auxiliares que quieras.

Las reglas para convertir una palabra a Pig Latin son las siguientes:

1.- Para las palabras que comienzan por consonante, todas las letras antes de
la vocal inicial son movidas al final de la palabra y se añade "ay". Por
ejemplo:
    - pig     => igpay
    - latin   => atinlay
    - banana  => ananabay
    - friends => iendsfray
    - smile   => ilesmay
    - string  => ingstray

2.- Para las palabras que comienzan por vocal, simplemente añade "way" al final
de la palabra. Por ejemplo:
    - eat    => eatway
    - omelet => omeletway
    - are    => areway
    - I      => Iway

Ten en cuenta además que: si una palabra empieza por mayúscula la palabra en
Pig Latin también tiene que empezar por mayúscula.
"""


def get_word_from_a_phrase(sentence: str) -> list[str]:
    space: str = " "
    word_list: list[str] = []
    word: str = ""
    sentence += " "
    for letter in sentence:
        if letter not in space:
            word += letter
        else:
            word_list.append(word)
            word = ""
    return word_list


get_word_from_a_phrase("hola mundo soy vegeta el mejor youtuber")


def pig_lagin(sentence: str) -> str:
    word_list: list[str] = []
    word_list.append(get_word_from_a_phrase(sentence))


"""
TODO Tengo la palabra de la frase tengo que traduciarla y meterla al string
    vowels_list: str = ["a", "e", "i", "o", "u"]
        translated_phrase: str
      for letter in sentence:
        if sentence.startswith(vowels_list.lower) or sentence.startswith(vowels_list.upper):
            sentence+"way"
        else  
"""
