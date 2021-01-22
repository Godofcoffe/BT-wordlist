from gerador.gerador import *
from time import sleep
from interface.form_texto import *
from interface.menu import *
from BD.teste_arquivo import *

#para saber mais sobre a geração de caractéres, acesse a biblioteca gerador.
#                Sr.Azul™               #


def escolha(nome):
	while True:
		escolha = str(input(nome))
		escolha = (f'{escolha.strip().lower()}')
		if escolha == 's':
			return True
			break
		elif escolha == 'n':
			return False
			break
		else:
			cor_texto('vermelho','Escolha entre as duas opções!')
			pass



print(linha())
print('Gerador'.center(43))
print(linha())

p = 'carácteres.txt'
s = 'números.txt'
pc = 'WiFi.txt'

while True:
	opc = menu_principal(['Padrão','Wifi'])
# A opção padrão pode ser usada para força bruta em contas que usam apps de geração de senha ou para Wifis com senhas de fábrica.
	if opc == 1:
		opc = escolha('Deseja adição de simbolos? [s/n]:')
		opc2 = escolha('Deseja adição de letras maiuscúlas? [s/n]:')
		criar_arqv(p)
		if opc == opc2 == True :
			print('Para uma wordlist consideravel,deixe programa rodar por no minimo 5 minutos.')
			sleep(3)
			ms = []
			print('gerando...')
			sleep(2)
			while True:
				a = rand(None,True
				,False,True)
				while not a in ms:
					cor_texto('vermelho',a)
					ms.append(a)
					add_w(p,a)
		elif opc == opc2 == False:
			print('Para uma wordlist consideravel,deixe programa rodar por no minimo 5 minutos.')
			sleep(3)
			ms = []
			print('gerando...')
			sleep(2)
			while True:
				a = rand(None,False
				,False,False)
				while not a in ms:
					cor_texto('vermelho',a)
					ms.append(a)
					add_w(p,a)
		
		elif opc == False and opc2 == True:
			print('Para uma wordlist consideravel,deixe programa rodar por no minimo 5 minutos.')
			sleep(3)
			ms = []
			print('gerando...')
			sleep(2)
			while True:
				a = rand(None,False
				,False,True)
				while not a in ms:
					cor_texto('vermelho',a)
					ms.append(a)
					add_w(p,a)
		elif opc == True and opc2 == False:
			print('Para uma wordlist consideravel,deixe programa rodar por no minimo 5 minutos.')
			sleep(3)
			ms = []
			print('gerando...')
			sleep(2)
			while True:
				a = rand(None,True
				,False,False)
				while not a in ms:
					cor_texto('vermelho',a)
					ms.append(a)
					add_w(p,a)
		

	elif opc == 2:
# A opção wifi se aplica a senhas de segurança baixa, como números de telefone ou nomes de pessoas com datas ou números aleátorios.
		opc2 = menu_principal(
		['Números','Palavra-chave'])
		if opc2 == 1:
			criar_arqv(s)
			ms = []
			print('Para uma wordlist consideravel,deixe programa rodar por no minimo 5 minutos.')
			sleep(3)
			print('gerando...')
			sleep(2)
			while True:
				a = rand(None,False,True)
				while not a in ms:
					cor_texto('vermelho',a)
					ms.append(a)
					add_w(s,a)
			
		elif opc2 == 2:
			escolha = escolha('Deseja que a palavra esteja no inicio? [s/n]:')
			nome = str(input('Qual o palavra:'))
			criar_arqv(pc)
			if escolha == True:
				ms = []
				print('gerando...')
				sleep(2)
				while True:
					a = rand(nome,False
					,False,False,True)
					while not a in ms:
						cor_texto('vermelho',a)
						ms.append(a)
						add_w(pc,a)
			elif escolha == False:
				ms = []
				print('gerando...')
				sleep(2)
				while True:
					a = rand(nome,False
					,False,False,False)
					while not a in ms:
						cor_texto('vermelho',a)
						ms.append(a)
						add_w(pc,a)
					
		elif opc2 == 3:
			print('saindo...')
			sleep(1)
			break
	elif opc == 3:
		print('saindo...')
		sleep(1)
		break