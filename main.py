from colorama import init
from time import sleep
from db.files import *
from generator.generator import *
from interface.menu import *
from interface.form_text import *


def esc(valid):
    while True:
        entry = str(input(valid))
        entry = f'{entry.strip().lower()}'
        if entry == 'y':
            return True
        elif entry == 'n':
            return False
        else:
            print(color_text('yellow', 'Choose between the two options!'))
            pass


class Together(Rand):
    def __init__(self, path, limite, name=None, simb=False, num=False, cap=False, pos=False, limit=8):
        super().__init__(name, simb, num, cap, pos, limit)
        self.path = path
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
folder = 'well/'
init()

while True:
    header('Generator')
    opc = main_menu(['Standard', 'Wifi'])
    # A opção padrão pode ser usada para força bruta em contas que usam apps de geração de senha
    if opc == 1:
        opc = esc('Do you want to add symbols? [y/n]: ')
        opc2 = esc('Do you want to add capital letters? [y/n]: ')
        mkarq(folder+OUT_TXT)
        attempts = int(input('Before generating us, how many attempts do you want to save ?: '))
        if opc and opc2:
            Together(OUT_TXT, attempts, None, True, False, True).run()

        elif not opc and not opc2:
            Together(OUT_TXT, attempts).run()

        elif not opc and opc2:
            Together(OUT_TXT, attempts, None, False, False, True).run()

        elif opc and not opc2:
            Together(OUT_TXT, attempts, name=None, simb=True).run()

    elif opc == 2:
        # A opção wifi se aplica a senhas de segurança baixa,
        # como números de telefone ou nomes de pessoas com datas ou números aleátorios.
        opc2 = main_menu(['Numbers', 'Keyword', 'Default password'])
        if opc2 == 1:
            mkarq(folder+OUT_NUM)
            attempts = int(input('Before generating us, how many attempts do you want to save ?: '))
            Together(OUT_NUM, attempts, None, False, True).run()

        elif opc2 == 2:
            selection = esc('Do you want the word to be at the beginning? [y/n]: ')
            nome = str(input('What is the word: '))
            mkarq(folder+OUT_WIFI)
            attempts = int(input('Before generating us, how many attempts do you want to save ?: '))
            if selection:
                Together(OUT_WIFI, attempts, nome, False, False, False, True).run()
            elif not selection:
                Together(OUT_WIFI, attempts, nome).run()

        elif opc2 == 3:
            # A diferença aqui que em vez de 8 caracteres serão 10.
            mkarq(folder+OUT_ROT)
            attempts = int(input('Before generating us, how many attempts do you want to save ?: '))
            Together(OUT_ROT, attempts, None, False, False, True, False, 10).run()

        elif opc2 == 4:
            print(color_text('white', 'exiting...'))
            sleep(1)
            break
    elif opc == 3:
        print(color_text('white', 'exiting...'))
        sleep(1)
        break
