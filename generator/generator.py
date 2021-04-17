from random import randint, choice


class Rand:
    def __init__(self, name, simb, num, cap, pos, limit):
        self.name = name
        self.simb = simb
        self.num = num
        self.cap = cap
        self.pos = pos
        self.limit = limit

    def rand(self):
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

        # geração de números
        attempts = []
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'x', 'y', 'z']
        if self.num:
            for c in range(0, 8):
                a = randint(0, 9)
                attempts.append(str(a))
        elif not self.num:
            for c in range(0, 8):
                a = randint(0, 9)
                attempts.append(str(a))

            # geração da palavra-chave
            if self.name is not None:
                lenght = len(self.name)
                attempts2 = []
                for c in range(0, 8 - lenght + 1):
                    a = randint(0, 9)
                    attempts2.append(str(a))
                if self.pos:
                    attempts2.insert(0, self.name)
                    result = ''.join(attempts2)
                    return result
                elif not self.pos:
                    attempts2.append(self.name)
                    result = ''.join(attempts2)
                    return result

            # parte da geração aleatória
            if self.name is None:
                letters2 = letters[:]
                if self.cap:
                    for l in letters:
                        letters2.append(l.upper())
                if not self.cap:
                    pass
                if self.simb:
                    letters2.append('#')
                    letters2.append('@')
                    letters2.append('+')
                    letters2.append('%')
                    letters2.append('$')
                    letters2.append('!')
                    letters2.append('?')
                    letters2.append('&')
                    letters2.append('*')
                if not self.simb:
                    pass
                for l in letters2:
                    attempts.append(l)

        # escolha dos 8 dígitos ou mais
        temp = []
        for c in range(self.limit):
            temp.append(choice(attempts))
        result = ''.join(temp)
        return result
