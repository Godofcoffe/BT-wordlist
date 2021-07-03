from random import randint, choice
from src.interface.menu import color_text
from time import sleep

res_combine = 1


def factorial(num: int):
    tot = 1
    for n in range(1, num + 1):
        tot *= n
    return tot


def combine(n: int, p: int):
    return int(factorial(n) / (factorial(p) * factorial(n - p)))


def rand(word=None, symbols=False, only_numbers=False, numbers=False, uppers=False, position=False, limit=8):
    """
Generates a random password of 8 or more characters between letters and numbers.
    name = word you want to add to the generator:
    if a word is added, only random numbers will be generated that will fill the space to the limit.
    max = maximum number that will be generated.
    simb = chooses whether to add symbols.
    num = choose whether there will be only numbers.
    cap = choose if there will be capital letters.
    pos = Changes the position of the name parameter.
"""

    result: str = ''
    letters = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'x', 'y', 'z'
    )
    global res_combine
    # geração de números
    if only_numbers:
        for c in range(0, limit):
            result += str(randint(0, 9))
        res_combine = factorial(limit)
    else:
        # geração da palavra-chave
        if word is not None:
            lenght = len(word)
            if numbers:
                for c in range(0, limit - lenght + 1):
                    result += str(randint(0, 9))
            elif not numbers:
                for c in range(0, limit - lenght + 1):
                    result += choice(letters)
            res_combine = factorial(len(result))
            if position:
                result = word + result
            elif not position:
                result += word

        # parte da geração aleatória
        if word is None:
            letters2 = list(letters[:])
            if uppers:
                for letter in letters:
                    letters2.append(letter.upper())
            if symbols:
                letters2.append('#')
                letters2.append('@')
                letters2.append('+')
                letters2.append('%')
                letters2.append('$')
                letters2.append('!')
                letters2.append('?')
                letters2.append('&')
                letters2.append('*')
            if numbers:
                for c in range(9):
                    letters2.append(c)
            for c in range(limit):
                result += str(choice(letters2))
            res_combine = factorial(limit)
    return result


def main(archive: str, **kwargs):
    word = kwargs.get("word")
    simb = kwargs.get("symbols")
    if simb is None:
        simb = False

    only_num = kwargs.get("only_num")
    if only_num is None:
        only_num = False

    num = kwargs.get("numbers")
    if num is None:
        num = False

    cap = kwargs.get("uppers")
    if cap is None:
        cap = False

    pos = kwargs.get("position")
    if pos is None:
        pos = False

    limit = kwargs.get("limit")
    if limit is None:
        limit = 8

    possibilities = {}
    print(f"Were calculated {res_combine} possibilities")
    print(color_text('white', 'generating ...'))
    sleep(3)
    with open(archive, "w+") as out:
        for c in range(50):
            retorn = rand(word, simb, only_num, num, cap, pos, limit)
            possibilities[retorn] = 0
            if possibilities[retorn] > 1:
                print(color_text("red", retorn))
            else:
                print(color_text('green', retorn))
                possibilities[retorn] += 1
                out.write(retorn)
