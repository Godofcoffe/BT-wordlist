from interface.form_text import *


def linha(tam=43):
    """
Returns the number of the argument size. Remembering that the size is in pixels.
    """
    return '-' * tam


def teste_int(num):
    """
Tests the data and returns if it is an integer. It replaces the input function.
    """
    while True:
        try:
            n = int(input(num))
        except (ValueError, NameError):
            print(color_text('red', 'Error, try again!'))
        except KeyboardInterrupt:
            print(color_text('red', 'The user chose not to enter the data!'))
        except TypeError:
            print(color_text('red', 'Data mismatch error!'))
        else:
            return n


def cabeçalho(txt):
    """
Just type the text in the argument and it will be printed and centralized.
    """
    print(linha())
    print(color_text('green', f'{txt.center(43)}'))
    print(linha())


def menu_principal(opc):
    """
A main little boy ready.
   opc = options in LIST.
There is no need for the exit option, the code does it automatically.
    """
    c = 1
    e = 'Exit the program.'
    for item in opc:
        print(color_text('white', f'[ {c} ]'), f'- {item}')
        c += 1
    print(color_text('white', f'[ {c} ]'), f'- {e}')
    print(linha())
    print(color_text('yellow', 'Enter a number: '), end='')
    opc = teste_int('')
    if opc > c:
        print(color_text('red', 'You have crossed the limit of options!'))
    elif opc == 0:
        print(color_text('red', 'There is no option 0!'))
    return opc
