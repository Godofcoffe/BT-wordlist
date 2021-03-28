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
    Gera uma senha aleátoria de 8 ou mais caracteres entre letras e números.
      name = palavra que queira adicionar no gerador:
      se for adicionado uma palavra,só serão gerados números aleatórios que vão preencher o espaço ate o limite.
      max = número máximo que será gerado.
      simb = escolhe se haverá adição de simbolos.
      num = escolhe se haverá apenas números.
      cap = escolhe se haverá letras maiuscúlas.
      pos = Muda a posição do parâmetro name.
    """

        # geração de números
        tentativas = []
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'x', 'y', 'z']
        if self.num:
            for c in range(0, 8):
                a = randint(0, 9)
                tentativas.append(str(a))
        elif not self.num:
            for c in range(0, 8):
                a = randint(0, 9)
                tentativas.append(str(a))

            # geração da palavra-chave
            if self.name is not None:
                lenght = len(self.name)
                tentativas2 = []
                for c in range(0, 8 - lenght + 1):
                    a = randint(0, 9)
                    tentativas2.append(str(a))
                if self.pos:
                    tentativas2.insert(0, self.name)
                    produto = ''.join(tentativas2)
                    return produto
                elif not self.pos:
                    tentativas2.append(self.name)
                    produto = ''.join(tentativas2)
                    return produto

            # parte da geração aleatória
            if self.name is None:
                letras2 = letras[:]
                if self.cap:
                    for l in letras:
                        letras2.append(l.upper())
                if not self.cap:
                    pass
                if self.simb:
                    letras2.append('#')
                    letras2.append('@')
                    letras2.append('+')
                    letras2.append('%')
                    letras2.append('$')
                    letras2.append('!')
                    letras2.append('?')
                    letras2.append('&')
                    letras2.append('*')
                if not self.simb:
                    pass
                for l in letras2:
                    tentativas.append(l)

        # escolha dos 8 dígitos
        temp = []
        for c in range(self.limit):
            temp.append(choice(tentativas))
        produto = ''.join(temp)
        return produto
