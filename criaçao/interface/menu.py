from interface.form_texto import *

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
		except (ValueError,NameError):
			print('\033[31m{}\033[m'.format('Erro!tente novamente!'))
		except Keyboardinterrupt:
			print('\033[31m{}\033[m'.format('O usuário escolheu não digitar os dados!'))
		except TypeError:
			print('\033[31m{}\033[m'.format('Erro de discordância de dados!'))
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
	e = ('Sair do programa.')
	for item in opc:
		print(f'\033[31m{c}\033[m - \033[32m{item}\033[m')
		c +=1
	print(f'\033[31m{c}\033[m - \033[32m{e}\033[m')
	print(linha())
	opc = teste_int('Digite um número:')
	if opc > c:
		cor_texto('vermelho','Você passou do limite de opções!')
	elif opc == 0:
		cor_texto('vermelho','Não há opção 0!')
	return opc