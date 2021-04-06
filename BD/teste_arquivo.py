from interface.menu import *
from interface.form_text import *


def arquivo_existe(nome):
    """
Tests if the file exists, just argue the file name.
    """
    try:
        open(nome, 'rt')
    except FileExistsError or PermissionError:
        return False
    else:
        return True


def criar_arqv(nome):
    """
Create a new file, just argue the file name.
    """
    try:
        open(nome, 'wt+')
    except:
        print(color_text('red', 'Error creating the file'))


def ler_arqv(nome):
    """
Print the txt file, just argue the file name.
    """
    try:
        open(nome, 'rt')
    except FileExistsError or PermissionError:
        print(color_text('red', 'ERROR reading file'))
    else:
        with open(nome, 'rt') as arqv:
            cabeçalho('SAVED DATA.')
            for linha in arqv:
                print(f'{linha}'.replace('\n', ''))


def add_w(arq, arg1='vazio'):
    """
Attempts for the wordlist will be added here.
    """
    try:
        open(arq, 'at')
    except FileExistsError or PermissionError:
        print(color_text('red', 'Error opening file.'))
    else:
        try:
            with open(arq, 'at') as arqv:
                arqv.write(f'{arg1}\n')
        except FileExistsError or PermissionError:
            print(color_text('red', 'Error adding to WordList.'))
