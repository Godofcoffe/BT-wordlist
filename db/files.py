from interface.menu import *
from interface.form_text import *


def file_exist(nome):
    """
Tests if the file exists, just argue the file name.
    """
    try:
        open(nome, 'rt')
    except FileExistsError or PermissionError:
        return False
    else:
        return True


def mkarq(nome):
    """
Create a new file, just argue the file name.
    """
    try:
        open(nome, 'wt+')
    except Exception as error:
        print(color_text('red', f'Error creating the file {error}'))


def lenarq(nome):
    """
Print the txt file, just argue the file name.
    """
    try:
        open(nome, 'rt')
    except FileExistsError or PermissionError:
        print(color_text('red', 'ERROR reading file'))
    else:
        with open(nome, 'rt') as arqv:
            main_menu('SAVED DATA.')
            for line in arqv:
                print(f'{line}'.replace('\n', ''))


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
