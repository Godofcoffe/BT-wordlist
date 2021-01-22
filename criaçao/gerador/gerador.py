import random

def rand(nome=None,simb=False,num = False,cap= False,pos=False,max=9):
	"""
Gera uma senha aleátoria de 8 caracteres entre letras e números.
  nome = palavra que queira adicionar no gerador:
  	se for adicionado uma palavra,só serão gerados números aleatórios que vão preencher o espaço de 8 caractéres.
  max = número máximo que será gerado.
  simb = escolhe se haverá adição de simbolos.
  num = escolhe se haverá apenas números.
  cap = escolhe se haverá letras maiuscúlas.
  pos = Muda a posição do parâmetro nome.
	"""

# geração de números
	if num == True:
		a = random.randint(0,max)
		b = random.randint(0,max)
		c = random.randint(0,max)
		d = random.randint(0,max)
		e = random.randint(0,max)
		f = random.randint(0,max)
		g = random.randint(0,max)
		h = random.randint(0,max)
		tentativas = [a,b,c,f,e,f,g,h]
	elif num == False:
		a = random.randint(0,max)
		b = random.randint(0,max)
		c = random.randint(0,max)
		d = random.randint(0,max)
		e = random.randint(0,max)
		f = random.randint(0,max)
		g = random.randint(0,max)
		h = random.randint(0,max)
		tentativas = [a,b,c,f,e,f,g,h]


#geração da palavra-chave
		if nome != None:
			lern= len(nome)
			numeros = [a,b,c,f,e,f,g,h]
			tentativas = []
			for num in numeros:
				a = str(num)
				tentativas.append(a)
			numeros.clear()
			lerl = len(tentativas)
			if lern < lerl:
				x = 0
				while lern > x:
					tentativas.pop()
					x += 1
			if pos == False:
				tentativas.append(nome)
			elif pos == True:
				tentativas.insert(0, nome)
			tentativas = ''.join(tentativas)
			return tentativas
			
			
		letras =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
#parte da geração aleatória
		if nome == None:
			if cap == True:
				temp = letras[:]
				cap = []
				for letra in temp:
					cap.append(f'{letra.upper()}')
				temp.clear()
				for letra in cap:
					letras.append(letra)
				cap.clear()
			elif cap == False:
				pass
			if simb == True:
				letras.append('#')
				letras.append('@')
				letras.append('+')
				letras.append('%')
				letras.append('$')
				letras.append('!')
				letras.append('?')
				letras.append('&')
				letras.append('*')
				a1 = random.choice(letras)
				b2 = random.choice(letras)
				c3 = random.choice(letras)
				d4 = random.choice(letras)
				e5 = random.choice(letras)
				f6 = random.choice(letras)
				g7 = random.choice(letras)
				h8 = random.choice(letras)
				tentativas.append(a1)
				tentativas.append(b2)
				tentativas.append(c3)
				tentativas.append(d4)
				tentativas.append(e5)
				tentativas.append(f6)
				tentativas.append(g7)
				tentativas.append(h8)
			elif simb == False:
				a1 = random.choice(letras)
				b2 = random.choice(letras)
				c3 = random.choice(letras)
				d4 = random.choice(letras)
				e5 = random.choice(letras)
				f6 = random.choice(letras)
				g7 = random.choice(letras)
				h8 = random.choice(letras)
				tentativas.append(a1)
				tentativas.append(b2)
				tentativas.append(c3)
				tentativas.append(d4)
				tentativas.append(e5)
				tentativas.append(f6)
				tentativas.append(g7)
				tentativas.append(h8)


# escolha dos 8 dígitos
	prim = random.choice(tentativas)
	seg = random.choice(tentativas)
	ter = random.choice(tentativas)
	quar = random.choice(tentativas)
	quin = random.choice(tentativas)
	sext = random.choice(tentativas)
	set = random.choice(tentativas)
	oit = random.choice(tentativas)
	temp = [prim,seg,ter,quar,quin,sext,set,oit]
	wl = []
	for c in temp:
		a = str(c)
		wl.append(a)
	temp.clear()
	tentativas0 = ''.join(wl)
	return tentativas0