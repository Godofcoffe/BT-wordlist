from colorama import init
from time import sleep
from db.files import *
from os import path, mkdir
from generator.generator import *
from interface.menu import *
from interface.form_text import *


def esc(valid):
    while True:
        entry = str(input(valid)).strip().lower()[0]
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
if not path.exists(folder):
    mkdir(folder)

while True:
    header('Generator')
    opc = main_menu(['Standard', 'Wifi'])
    # A opção padrão pode ser usada para força bruta em contas que usam apps de geração de senha

    # A opção wifi se aplica a senhas de segurança baixa,
    # como números de telefone ou nomes de pessoas com datas ou números aleátorios.
    # ou quando voce sabe pelo menos um pedaço da senha


    if opc == 1:
        while True:
            opc = esc('Do you want to add symbols? [y/n]: ')
            opc2 = esc('Do you want to add capital letters? [y/n]: ')
            opc3 = esc('Want it to contain numbers? [y/n]: ')
            attempts = int(input('How many attempts/words: '))
            print()
            print(f'Procedures:\nsymbols: {opc}\ncapital letters: {opc2}\nnumbers: {opc3}\n{attempts} words')
            if esc('Continue...? [y/n]: '):
                mkarq(folder+OUT_TXT)
                if opc and opc2 and opc3:
                    Together(folder+OUT_TXT, attempts, None, True, True, True).run()

                elif not opc and not opc2 and not opc3:
                    Together(folder+OUT_TXT, attempts).run()

                elif not opc and opc2 and not opc3:
                    Together(folder+OUT_TXT, attempts, None, False, False, True).run()

                elif opc and not opc2 and not opc3:
                    Together(folder+OUT_TXT, attempts, None, True).run()
                
                elif not opc and not opc2 and opc3:
                    Together(folder+OUT_TXT, attempts, None, False, True).run()
                elif opc and opc2 and not opc3:
                    Together(folder+OUT_TXT, attempts, None, True).run()
                break
            else:
                break

    
    elif opc == 2:
        opc2 = main_menu(['Numbers', 'Keyword', 'Default password'])
        if opc2 == 1:
            mkarq(folder+OUT_NUM)
            attempts = int(input('Before generating us, how many attempts do you want to save ?: '))
            temp = []
            list_8char = []
            for c in range(attempts):
                for d in range(8):
                    var = randint(0, 9)
                    list_8char.append(str(var))
                result = ''.join(list_8char)
                list_8char.clear()
                if not result in temp:
                    print(color_text('green', result))
                    temp.append(result)
            for e in temp:
                add_w(folder+OUT_NUM, e)
        
        
        elif opc2 == 2:
            selection = esc('Do you want the word to be at the beginning? [y/n]: ')
            name = str(input('What is the word: '))
            attempts = int(input('Before generating us, how many attempts do you want to save ?: '))
            print('Spaces will be filled with random characters...')
            sleep(3)
            opc = esc('Do you want spaces to be numbers? [y/n]: ')
            print()
            print(f'Procedures:\nWord at the beginning: {selection}\nWord: {name}\nnumbers: {opc}\n{attempts} words')
            if esc('Continue...? [y/n]: '):
                mkarq(folder+OUT_WIFI)
                if selection and opc:
                    Together(folder+OUT_WIFI, attempts, name, False, True, False, True).run()
                elif selection and not opc:
                    Together(folder+OUT_WIFI, attempts, name, False, False, False, True).run()
                elif not selection and opc:
                    Together(folder+OUT_WIFI, attempts, name, False, True).run()


        elif opc2 == 3:
            # A diferença aqui que em vez de 8 caracteres serão 10.
            # aqui será usado normalmente para roteadores com senhas SSIDs de fabrica
            mkarq(folder+OUT_ROT)
            attempts = int(input('Before generating us, how many attempts do you want to save ?: '))
            Together(folder+OUT_ROT, attempts, None, False, False, True, False, 10).run()

        elif opc2 == 4:
            print(color_text('white', 'exiting...'))
            sleep(1)
            break
    elif opc == 3:
        print(color_text('white', 'exiting...'))
        sleep(1)
        break
