def st_texto(s,txt):
	"""
Para editar a fonte do texto:
	s = 'sublinhado,negativo ou negrito'
	txt = 'texto'
Uso obrigatorio de aspas simples.
	"""
	if s == 'negrito':
		print('\033[1m{}\033[m'.format(txt))
	elif s == 'sublinhado':
		print('\033[4m{}\033[m'.format(txt))
	elif s == 'negativo':
		print('\033[7m{}\033[m'.format(txt))


def cor_texto(c,txt):
	"""
Para editar a cor do texto:
	c = 'cor'
	txt = 'texto'
Uso obrigatorio de aspas simples.
	"""
	if c == 'vermelho':
		print('\033[31m{}\033[m'.format(txt))
	elif c == 'branco':
		print('\033[30m{}\033[m'.format(txt))
	elif c == 'verde':
		print('\033[32m{}\033[m'.format(txt))
	elif c == 'amarelo':
		print('\033[33m{}\033[m'.format(txt))
	elif c == 'azul':
		print('\033[34m{}\033[m'.format(txt))
	elif c == 'ciano':
		print('\033[36m{}\033[m'.format(txt))
	elif c == 'cinza':
		print('\033[37m{}\033[m'.format(txt))


def fundo_texto(c,txt):
	"""
Para editar o fundo do texto:
		c = 'cor'
		txt = 'texto'
Uso obrigatorio de aspas simples.
	"""
	if c == 'vermelho':
		print('\033[41m{}\033[m'.format(txt))
	elif c == 'branco':
		print('\033[40m{}\033[m'.format(txt))
	elif c == 'verde':
		print('\033[42m{}\033[m'.format(txt))
	elif c == 'amarelo':
		print('\033[43m{}\033[m'.format(txt))
	elif c == 'azul':
		print('\033[44m{}\033[m'.format(txt))
	elif c == 'ciano':
		print('\033[46m{}\033[m'.format(txt))
	elif c == 'cinza':
		print('\033[47m{}\033[m'.format(txt))