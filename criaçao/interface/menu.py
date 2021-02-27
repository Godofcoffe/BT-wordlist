def linha(tam=43):
    """
Retorna o número do tamanho da argumentação. Lembrando que o tamanho é em pixels.
    """
    return '-' * tam


def teste_int(num):
    """
Testa os dados e retorna se for um número inteiro.Ele substitue a função input.
    """
    while True:
        try:
            n = int(input(num))
        except (ValueError, NameError):
            print('Erro!tente novamente!')
        except KeyboardInterrupt:
            print('O usuário escolheu não digitar os dados!')
        except TypeError:
            print('Erro de discordância de dados!')
        else:
            return n


def cabeçalho(txt):
    """
Apenas digite o texto na argumentação e ele será imprimido e centralizado.
    """
    print(linha())
    print(txt.center(43))
    print(linha())


def menu_principal(opc):
    """
Um menuzinho principal pronto.
  opc = opções em LISTA.
Não é necessario a opção de saida,o código faz automaticamente.
    """
    c = 1
    e = 'Sair do programa.'
    for item in opc:
        print(f'{c} - {item}')
        c += 1
    print(f'{c} - {e}')
    print(linha())
    opc = teste_int('Digite um número:')
    if opc > c:
        print('Você passou do limite de opções!')
    elif opc == 0:
        print('Não há opção 0!')
    return opc
