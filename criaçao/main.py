from time import sleep
from BD.teste_arquivo import *
from gerador.gerador import *


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


def gerarlist(caminho, limite, *args):
    ms = []
    print('gerando...')
    sleep(2)
    for c in range(limite):
        retorno = rand(args)
        if retorno not in ms:
            cor_texto('vermelho', retorno)
            ms.append(retorno)
            add_w(caminho, retorno)


# saida de arquivos .txt
OUT_TXT = 'carácteres.txt'
OUT_NUM = 'números.txt'
OUT_WIFI = 'WiFi.txt'
OUT_ROT = 'Roteador.txt'

while True:
    cabeçalho('Gerador')
    opc = menu_principal(['Padrão', 'Wifi'])
    # A opção padrão pode ser usada para força bruta em contas que usam apps de geração de senha
    if opc == 1:
        opc = esc('Deseja adição de simbolos? [s/n]:')
        opc2 = esc('Deseja adição de letras maiuscúlas? [s/n]:')
        criar_arqv(OUT_TXT)
        tentativas = int(input('Antes de gerar-mos, quantas tentativas deseja salvar?: '))
        if opc and opc2:
            gerarlist(OUT_TXT, tentativas, None, True, False, True, False, 8)

        elif not opc and not opc2:
            gerarlist(OUT_TXT, tentativas, None, False, False, False, False, 8)

        elif not opc and opc2:
            gerarlist(OUT_TXT, tentativas, None, False, False, True, False, 8)

        elif opc and not opc2:
            gerarlist(OUT_TXT, tentativas, None, True, False, False, False, 8)

    elif opc == 2:
        # A opção wifi se aplica a senhas de segurança baixa,
        # como números de telefone ou nomes de pessoas com datas ou números aleátorios.
        opc2 = menu_principal(['Números', 'Palavra-chave', 'Senha padrão'])
        if opc2 == 1:
            criar_arqv(OUT_NUM)
            tentativas = int(input('Antes de gerar-mos, quantas tentativas deseja salvar?: '))
            gerarlist(OUT_NUM, tentativas, None, False, True, False, False, 8)

        elif opc2 == 2:
            escolha = esc('Deseja que a palavra esteja no inicio? [s/n]:')
            nome = str(input('Qual o palavra:'))
            criar_arqv(OUT_WIFI)
            tentativas = int(input('Antes de gerar-mos, quantas tentativas deseja salvar?: '))
            if escolha:
                gerarlist(OUT_WIFI, tentativas, nome, False, False, False, True, 8)
            elif not escolha:
                gerarlist(OUT_WIFI, tentativas, nome, False, False, False, False, 8)

        elif opc2 == 3:
            # A diferença aqui que em vez de 8 caracteres serão 10.
            criar_arqv(OUT_ROT)
            tentativas = int(input('Antes de gerar-mos, quantas tentativas deseja salvar?: '))
            gerarlist(OUT_ROT, tentativas, None, False, False, True, False, 10)

        elif opc2 == 4:
            print('saindo...')
            sleep(1)
            break
    elif opc == 3:
        print('saindo...')
        sleep(1)
        break
