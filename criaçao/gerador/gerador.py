from random import randint, choice


def rand(nome=None, simb=False, num=False, cap=False, pos=False):
    """
Gera uma senha aleátoria de 8 caracteres entre letras e números.
  nome = palavra que queira adicionar no gerador:
  se for adicionado uma palavra,só serão gerados números aleatórios que vão preencher o espaço de 8 caractéres.
  max = número máximo que será gerado.
  simb = escolhe se haverá adição de simbolos.
  num = escolhe se haverá apenas números.
  cap = escolhe se haverá letras maiuscúlas.
  pos = Muda a posição do parâmetro nome.
"""

    # geração de números
    tentativas = []
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'x', 'y', 'z']
    if num:
        for c in range(0, 8):
            a = randint(0, 9)
            tentativas.append(str(a))
    elif not num:
        for c in range(0, 9):
            a = randint(0, 9)
            tentativas.append(str(a))

        # geração da palavra-chave
        if nome is not None:
            lenght = len(nome)
            tentativas2 = []
            for c in range(0, 8 - lenght + 1):
                a = randint(0, 9)
                tentativas2.append(str(a))
            if pos:
                tentativas2.insert(0, nome)
                produto = ''.join(tentativas2)
                return produto
            elif not pos:
                tentativas2.append(nome)
                produto = ''.join(tentativas2)
                return produto

        # parte da geração aleatória
        if nome is None:
            letras2 = letras[:]
            if cap:
                for l in letras:
                    letras2.append(l.upper())
            if not cap:
                pass
            if simb:
                letras2.append('#')
                letras2.append('@')
                letras2.append('+')
                letras2.append('%')
                letras2.append('$')
                letras2.append('!')
                letras2.append('?')
                letras2.append('&')
                letras2.append('*')
            if not simb:
                pass
            for l in letras2:
                tentativas.append(l)

    # escolha dos 8 dígitos
    temp = []
    for c in range(0, 8):
        temp.append(choice(tentativas))
    produto = ''.join(temp)
    return produto
