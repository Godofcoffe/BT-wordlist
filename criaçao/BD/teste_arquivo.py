from criaçao.interface.menu import *
from criaçao.interface.form_texto import *


def arquivo_existe(nome):
    """
Testa se o arquivo existe,apenas argumente o nome do arquivo.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def criar_arqv(nome):
    """
Cria um novo arquivo,apenas argumente o nome do arquivo.
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo')


def ler_arqv(nome):
    """
Imprime o arquivo txt,apenas argumente o nome do arquivo.
    """
    try:
        a = open(nome, 'rt')
    except:
        cor_texto('ERRO ao ler arquivo')
    else:
        cabeçalho('DADOS SALVOS.')
        for linha in a:
            print(f'{linha}'.replace('\n', ''))
    finally:
        a.close()


def add_w(arq, arg1='vazio'):
    """
Aqui serão adicionados as tentativas para a wordlist.
    """
    try:
        a = open(arq, 'at')
    except:
        cor_texto('vermelho', 'Erro ao abrir arquivo.')
    else:
        try:
            a.write(f'{arg1}\n')
        except:
            cor_texto('vermelho', 'Erro ao adicionar a WordList.')
        else:
            pass
            a.close()
