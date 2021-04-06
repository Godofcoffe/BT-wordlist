from colorama import init
from time import sleep
from BD.teste_arquivo import *
from gerador.gerador import *
from interface.menu import *
from interface.form_text import *


def esc(valid):
    while True:
        opcao = str(input(valid))
        opcao = f'{opcao.strip().lower()}'
        if opcao == 'y':
            return True
        elif opcao == 'n':
            return False
        else:
            print(color_text('yellow', 'Choose between the two options!'))
            pass


class Concatenar(Rand):
    def __init__(self, caminho, limite, name=None, simb=False, num=False, cap=False, pos=False, limit=8):
        super().__init__(name, simb, num, cap, pos, limit)
        self.path = caminho
        self.total = limite

    def run(self):
        ms = []
        print(color_text('white', 'generating ...'))
        sleep(2)
        for c in range(self.total):
            retorno = self.rand()
            if retorno not in ms:
                print(color_text('green', retorno))
                ms.append(retorno)
                add_w(self.path, retorno)


# saida de arquivos .txt
OUT_TXT = 'characters.txt'
OUT_NUM = 'numbers.txt'
OUT_WIFI = 'WiFi.txt'
OUT_ROT = 'Router.txt'
init()

while True:
    cabeçalho('Generator')
    opc = menu_principal(['Standard', 'Wifi'])
    # A opção padrão pode ser usada para força bruta em contas que usam apps de geração de senha
    if opc == 1:
        opc = esc('Do you want to add symbols? [y/n]: ')
        opc2 = esc('Do you want to add capital letters? [y/n]: ')
        criar_arqv(OUT_TXT)
        tentativas = int(input('Before generating us, how many attempts do you want to save ?: '))
        if opc and opc2:
            Concatenar(OUT_TXT, tentativas, None, True, False, True).run()

        elif not opc and not opc2:
            Concatenar(OUT_TXT, tentativas).run()

        elif not opc and opc2:
            Concatenar(OUT_TXT, tentativas, None, False, False, True).run()

        elif opc and not opc2:
            Concatenar(OUT_TXT, tentativas, name=None, simb=True).run()

    elif opc == 2:
        # A opção wifi se aplica a senhas de segurança baixa,
        # como números de telefone ou nomes de pessoas com datas ou números aleátorios.
        opc2 = menu_principal(['Numbers', 'Keyword', 'Default password'])
        if opc2 == 1:
            criar_arqv(OUT_NUM)
            tentativas = int(input('Before generating us, how many attempts do you want to save ?: '))
            Concatenar(OUT_NUM, tentativas, None, False, True).run()

        elif opc2 == 2:
            escolha = esc('Do you want the word to be at the beginning? [y/n]: ')
            nome = str(input('What is the word: '))
            criar_arqv(OUT_WIFI)
            tentativas = int(input('Before generating us, how many attempts do you want to save ?: '))
            if escolha:
                Concatenar(OUT_WIFI, tentativas, nome, False, False, False, True).run()
            elif not escolha:
                Concatenar(OUT_WIFI, tentativas, nome).run()

        elif opc2 == 3:
            # A diferença aqui que em vez de 8 caracteres serão 10.
            criar_arqv(OUT_ROT)
            tentativas = int(input('Before generating us, how many attempts do you want to save ?: '))
            Concatenar(OUT_ROT, tentativas, None, False, False, True, False, 10).run()

        elif opc2 == 4:
            print(color_text('white', 'exiting...'))
            sleep(1)
            break
    elif opc == 3:
        print(color_text('white', 'exiting...'))
        sleep(1)
        break
