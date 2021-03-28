from interface.menu import *


def arquivo_existe(nome):
    """
Testa se o arquivo existe,apenas argumente o nome do arquivo.
    """
    try:
        open(nome, 'rt')
    except FileExistsError or PermissionError:
        return False
    else:
        return True


def criar_arqv(nome):
    """
Cria um novo arquivo,apenas argumente o nome do arquivo.
    """
    try:
        open(nome, 'wt+')
    except:
        print('Error creating the file')


def ler_arqv(nome):
    """
Imprime o arquivo txt,apenas argumente o nome do arquivo.
    """
    try:
        open(nome, 'rt')
    except FileExistsError or PermissionError:
        print('ERROR reading file')
    else:
        with open(nome, 'rt') as arqv:
            cabeçalho('SAVED DATA.')
            for linha in arqv:
                print(f'{linha}'.replace('\n', ''))


def add_w(arq, arg1='vazio'):
    """
Aqui serão adicionados as tentativas para a wordlist.
    """
    try:
        open(arq, 'at')
    except FileExistsError or PermissionError:
        print('Error opening file.')
    else:
        try:
            with open(arq, 'at') as arqv:
                arqv.write(f'{arg1}\n')
        except FileExistsError or PermissionError:
            print('Error adding to WordList.')
