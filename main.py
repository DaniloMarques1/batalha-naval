letters = {"A":0, "B":1, "C":2,"D":3,"E":4}

def celulasDisponiveis():
	m = []
	for i in range(10):
		for j in range(10):
			m.append([i,j])
	return m

celulas = celulasDisponiveis()
print(celulas)

def gerarTabuleiro():
	'''
	gera os tabuleiros da batalha
	'''
	import random
	t1 = []
	for i in range(10):
		linha = []
		for j in range(10):
			linha.append(random.randint(0,4))
		t1.append(linha)
	return t1


t1 = gerarTabuleiro();

def exibirTabuleiros(tabuleiro):
	'''
	Gera uma visualização do tabuleiro
	'''
	print(" ", end="")
	print(" A", end="")
	print(" B", end="")
	print(" C", end="")
	print(" D", end="")
	print(" E", end="")
	print(" F", end="")
	print(" G", end="")
	print(" H", end="")
	print(" I", end="")
	print(" J")
	for i in range(len(tabuleiro)):
		print(i,end="")
		for j in range(len(tabuleiro[0])):
			print(" x",end="")
		print()	

exibirTabuleiros(t1)	