from time import sleep
from BD.teste_arquivo import *
from gerador.gerador import *


# para saber mais sobre a geração de caractéres, acesse a biblioteca gerador.


def esc(valid):
    while True:
        opcao = str(input(valid))
        opcao = f'{opcao.strip().lower()}'
        if opcao == 's':
            return True
        elif opcao == 'n':
            return False
        else:
            cor_texto('vermelho', 'Escolha entre as duas opções!')
            pass


print(linha())
print('Gerador'.center(43))
print(linha())

p = 'carácteres.txt'
s = 'números.txt'
pc = 'WiFi.txt'
rp = 'Roteador.txt'

while True:
    opc = menu_principal(['Padrão', 'Wifi'])
    # A opção padrão pode ser usada para força bruta em contas que usam apps de geração de senha
    # ou para Wifis com senhas de fábrica.
    if opc == 1:
        opc = esc('Deseja adição de simbolos? [s/n]:')
        opc2 = esc('Deseja adição de letras maiuscúlas? [s/n]:')
        criar_arqv(p)
        if opc and opc2:
            print('Para uma wordlist consideravel,deixe programa rodar por no minimo 5 minutos.')
            sleep(3)
            ms = []
            print('gerando...')
            sleep(2)
            while True:
                a = rand(None, True, False, True)
                while a not in ms:
                    cor_texto('vermelho', a)
                    ms.append(a)
                    add_w(p, a)
        elif not opc and not opc2:
            print('Para uma wordlist consideravel,deixe programa rodar por no minimo 5 minutos.')
            sleep(3)
            ms = []
            print('gerando...')
            sleep(2)
            while True:
                a = rand(None, False, False, False)
                while a not in ms:
                    cor_texto('vermelho', a)
                    ms.append(a)
                    add_w(p, a)

        elif not opc and opc2:
            print('Para uma wordlist consideravel,deixe programa rodar por no minimo 5 minutos.')
            sleep(3)
            ms = []
            print('gerando...')
            sleep(2)
            while True:
                a = rand(None, False, False, True)
                while a not in ms:
                    cor_texto('vermelho', a)
                    ms.append(a)
                    add_w(p, a)
        elif opc and not opc2:
            print('Para uma wordlist consideravel,deixe programa rodar por no minimo 5 minutos.')
            sleep(3)
            ms = []
            print('gerando...')
            sleep(2)
            while True:
                a = rand(None, True, False, False)
                while a not in ms:
                    cor_texto('vermelho', a)
                    ms.append(a)
                    add_w(p, a)

    elif opc == 2:
        # A opção wifi se aplica a senhas de segurança baixa,
        # como números de telefone ou nomes de pessoas com datas ou números aleátorios.
        opc2 = menu_principal(
            ['Números', 'Palavra-chave', 'Senha padrão'])
        if opc2 == 1:
            criar_arqv(s)
            ms = []
            print('Para uma wordlist consideravel,deixe programa rodar por no minimo 5 minutos.')
            sleep(3)
            print('gerando...')
            sleep(2)
            while True:
                a = rand(None, False, True)
                while a not in ms:
                    cor_texto('vermelho', a)
                    ms.append(a)
                    add_w(s, a)

        elif opc2 == 2:
            escolha = esc('Deseja que a palavra esteja no inicio? [s/n]:')
            nome = str(input('Qual o palavra:'))
            criar_arqv(pc)
            if escolha:
                ms = []
                print('gerando...')
                sleep(2)
                while True:
                    a = rand(nome, False, False, False, True)
                    while a not in ms:
                        cor_texto('vermelho', a)
                        ms.append(a)
                        add_w(pc, a)
            elif not escolha:
                ms = []
                print('gerando...')
                sleep(2)
                while True:
                    a = rand(nome, False, False, False, False)
                    while a not in ms:
                        cor_texto('vermelho', a)
                        ms.append(a)
                        add_w(pc, a)
        elif opc2 == 3:
            # A diferença aqui que em vez de 8 caracteres serão 10.
            criar_arqv(rp)
            ms = []
            print('Para uma wordlist consideravel,deixe programa rodar por no minimo 5 minutos.')
            sleep(3)
            print('gerando...')
            sleep(2)
            while True:
                a = rand(None, False, False, True, max=10)
                while a not in ms:
                    cor_texto('vermelho', a)
                    ms.append(a)
                    add_w(rp, a)

        elif opc2 == 4:
            print('saindo...')
            sleep(1)
            break
    elif opc == 3:
        print('saindo...')
        sleep(1)
        break
