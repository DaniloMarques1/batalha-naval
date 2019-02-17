#Constantes
letters = {"A":0, "B":1, "C":2,"D":3,"E":4, "F":5, "G":6,"H":7,"I":8,"J":9}
#primeiro player
celulas1 = []
tabuleiro1 = []
submarinos1 = []
cruzadores1 = []
porta_avioes1 = []

#segundo jogador
celulas2 = []
tabuleiro2 = []
submarinos2 = []
cruzadores2 = []
porta_avioes2 = []
def main():
	#JOGADORES
	player1 = input("Nome do primeiro jogador: ")
	print("#" * 10)
	print("Gerando tabuleiros")
	print("#" * 10)
	#gerando submarinos primeiro player
	celulasDisponiveis(celulas1, tabuleiro1)
	gerarTabuleiro(celulas1, tabuleiro1, submarinos1, cruzadores1, porta_avioes1)
	
	#gerar navios segundo player
	player2 = input("Nome do segundo jogador: ")
	celulasDisponiveis(celulas2, tabuleiro2)
	gerarTabuleiro(celulas2, tabuleiro2, submarinos2, cruzadores2, porta_avioes2)
	
	#gerando fila player 1
	file = open("coordenadas.txt", "w")
	file.write("Coordenadas dos navios do jogador: {}\n".format(player1))
	file.write("Submarinos\n")
	file.write("{}\n".format(str(submarinos1)))
	file.write("Cruzadores: \n")
	file.write("{}\n".format(str(cruzadores1)))
	file.write("Porta avioes: \n")
	file.write("{}\n".format(str(porta_avioes1)))
	#gerando fila player 2
	file.write("Coordenadas dos navios do jogador: {}\n".format(player2))
	file.write("Submarinos\n")
	file.write("{}\n".format(str(submarinos2)))
	file.write("Cruzadores: \n")
	file.write("{}\n".format(str(cruzadores2)))
	file.write("Porta avioes: \n")
	file.write("{}\n".format(str(porta_avioes2)))
	file.close()
	#Continuar jogando até acabar os submarinos
	while True:
		if submarinos1 or submarinos2 or cruzadores1 or cruzadores2 or porta_avioes1 or porta_avioes2:
			if play(player2,tabuleiro1, submarinos1, cruzadores1, porta_avioes1) == 1:
				print("-" * 10)
				print("{} VENCEU O GAME".format(player2))
				print("-" * 10)
				break
			if play(player1,tabuleiro2, submarinos2, cruzadores2, porta_avioes2) == 1:
				print("-" * 10)
				print("{} VENCEU O GAME".format(player1))
				print("-" * 10)
				break

def play(player,tabuleiro, submarinos, cruzadores, porta_avioes):
	while True:
		print("VEZ DE: ", player)
		exibirTabuleiros(tabuleiro)
		while True:
			linha = input("Linha: ").upper()
			if linha >= "A" and linha <= "J":
				linha = letters[linha]
				break
		while True:
			coluna = int(input("Coluna: ")) - 1
			if coluna >= 0 and coluna <= 9:
				break
		coordenada = [linha, coluna]
		if not coordenada:
			break

		if hitASubmarino(coordenada, submarinos, tabuleiro) or hitACruzador(coordenada, cruzadores, tabuleiro) or hitPortaAviao(coordenada, porta_avioes, tabuleiro):
			print("FOGO")	
			if checkWin(submarinos, cruzadores, porta_avioes):	
				return 1
				
		else:
			print("-" * 10)
			print("AGUA")
			print("-" * 10)
			break
		

def checkWin(submarinos, cruzadores, porta_avioes):
	'''
	verifica se todos os navios foram destruidos, caso estejam vazios
	'''
	sub = True
	porta = True
	cru = True
	for i in submarinos:
		if len(i) != 0:
			sub = False
	for i in cruzadores:
		if len(i) != 0:
			cru = False
	for i in porta_avioes:
		if len(i) == 0:
			porta = False

	return sub and porta and cru	
def celulasDisponiveis(celulas,tabuleiro):
	'''
	gera todas as celulas disponiveis
	'''	
	for i in range(10):
		linha = []
		for j in range(10):
			celulas.append([i,j])
			linha.append("-")
		tabuleiro.append(linha)

def hitASubmarino(coordenada, submarinos, tabuleiro):
	'''
	coordenada: coordenada dada pelo usuario
	submarinos: matriz dos submarinos gerados aleatoriamente
	tabuleiro: tabuleiro do game
	'''
	#Submarino
	for i in submarinos:
		if coordenada in i:
			linha, coluna = coordenada[0], coordenada[1] 
			tabuleiro[linha][coluna] = "S"
			i.remove(coordenada)
			if len(i) == 0:
				print("Destruiu submarino")
			return True
	return False
				
def hitACruzador(coordenada, cruzadores, tabuleiro):
	'''
	coordenada: coordenada dada pelo usuario
	cruzadores: matriz dos cruzadores gerados aleatoriamente
	tabuleiro: tabuleiro do game
	'''
	for i in cruzadores:
		if coordenada in i:
			linha, coluna = coordenada[0], coordenada[1]
			tabuleiro[linha][coluna] = "C"
			i.remove(coordenada)
			if len(i) == 0:
				print("Destruiu cruzador")
			return True	
	return False

def hitPortaAviao(coordenada, porta_avioes, tabuleiro):
	'''
	coordenada: coordenada dada pelo usuario
	porta_avioes: matriz dos portas avioes gerados aleatoriamente
	tabuleiro: tabuleiro do game
	'''
	for i in porta_avioes:
		if coordenada in i:
			linha,coluna = coordenada[0], coordenada[1]
			tabuleiro[linha][coluna] = "P"
			i.remove(coordenada)
			if len(i) == 0:
				print("Destruiu porta aviao")
			return True
	return False			

def gerarTabuleiro(celulas, tabuleiro, submarinos, cruzadores, porta_avioes):
	'''
	celulas: celulas disponiveis para gerar os navios
	tabuleiro: as posições do jogo
	submarinos: a matriz que sera preenchida com as coordenadas dos submarino(s)
	cruzadores: a matriz que sera preenchida com as coordenadas dos cruzador(es)
	porta_avioes: a matriz que sera preenchida com as coordenadas dos porta_avioe(s)
	'''
	while True:
		sQtd = int(input("Quantos submarinos deseja entre 1 - 3: "))
		if sQtd >= 1 and sQtd <= 3:
			break

	for i in range(sQtd):
		while True:
			s1 = submarino(celulas)
			if s1 != -1:
				submarinos.append(s1)
				break
			#caso tenha removido alguma celula mas não tenha sido possivel formar um navio, resetar as celulas disponiveis
			celulasDisponiveis(celulas)
	print(submarinos)	
	#gerando os cruzadores
	
	while True:
		cQtd = int(input("Quantos cruzadores: entre 0 - 2: "))
		if cQtd >= 0 and cQtd <= 2:
			break
	for i in range(cQtd):
		while True:
			c1 = cruzador(celulas)
			if c1 != -1:
				cruzadores.append(c1)
				break
			#caso tenha removido alguma celula mas não tenha sido possivel formar um navio, resetar as celulas disponiveis	
			celulasDisponiveis(celulas, tabuleiro)
	print(cruzadores)

	#gerando os porta avioes

	while True:
		paQtd = int(input("Qunatos porta avioes: entre 0 - 1: "))
		if paQtd >=0 and paQtd <= 1:
			break
	for i in range(paQtd):
		while True:
			pa = porta_aviao(celulas)
			if pa != -1:
				porta_avioes.append(pa)
				break
			#caso tenha removido alguma celula mas não tenha sido possivel formar um navio, resetar as celulas disponiveis	
			celulasDisponiveis(celulas, tabuleiro)
	print(porta_avioes)

def exibirTabuleiros(tabuleiro):
	'''
	Gera uma visualização do tabuleiro
	'''
	print("#" * 12)
	print("* ", end="")
	for i in range(1, 11):
		print(f"{i}  ",end="")
	print()
	letter = 65	
	for i in range(10):
		print(f"{chr(letter)} ",end="")
		letter += 1
		for j in range(10):			
			print(f'{tabuleiro[i][j]:3}', end="")
		print()
	print("#" * 12)	
def direita(celulas,position, n):
	'''
	celulas: celulas disponiveis para geração do navio
	position: uma possivel posição para o navio
	n: quantas casas, a partir da primeira pular para a direita
	'''
	newPosition = [position[0], position[1] + n]
	if isAvailable(celulas,newPosition):
		return newPosition

def esquerda(celulas,position, n):
	'''
	celulas: celulas disponiveis para geração do navio
	position: uma possivel posição para o navio
	n: quantas casas, a partir da primeira pular para a esquerda
	'''
	newPosition = [position[0], position[1] - n]
	if isAvailable(celulas,newPosition):
		return newPosition

def up(celulas,position, n):
	'''
	celulas: celulas disponiveis para geração do navio
	position: uma possivel posição para o navio
	n: quantas casas, a partir da primeira pular para cima
	'''
	newPosition = [position[1] - n, position[1]]
	if isAvailable(celulas,newPosition):
		return newPosition

def down(celulas,position, n):
	'''
	celulas: celulas disponiveis para geração do navio
	position: uma possivel posição para o navio
	n: quantas casas, a partir da primeira pular para a baixo
	'''
	newPosition = [position[1] + n, position[1]]
	if isAvailable(celulas,newPosition):
		return newPosition


def submarino(celulas):
	'''
	celulas: celulas disponveis para geração do submarino
	retorna: uma matriz com as coordenadas do submarino gerado
	'''
	import random
	cel = []
	index = random.randint(0, len(celulas) - 1)
	firstPosition = celulas[index]
	celulas.remove(firstPosition)
	vertical = 0
	newPosition = direita(celulas,firstPosition, 1)
	if newPosition:
		cel.append(newPosition)
	else:
		newPosition = esquerda(celulas,firstPosition, 1)
		if newPosition:
			cel.append(newPosition)
		else:
			vertical = 1

	if vertical == 1:
		newPosition = down(celulas,firstPosition, 1)
		if newPosition:
			cel.append(newPosition)
		else:
			newPosition = up(firstPosition, 1)
			if newPosition:
				cel.append(newPosition)	
			else:
				return -1

				
	cel.append(firstPosition)
	return cel

def cruzador(celulas):
	'''
	celulas: celulas disponveis para geração do cruzador
	retorna: uma matriz com as coordenadas do cruzador gerado
	'''
	import random
	cel = []
	index = random.randint(0, len(celulas) - 1)
	firstPosition = celulas[index]
	celulas.remove(firstPosition)
	horizontal = 0
	vertical = 0
	newPosition1 = direita(celulas,firstPosition, 1)
	cel.append(firstPosition)

	#testa posições a direita
	if newPosition1:	
		newPosition2 = direita(celulas,firstPosition, 2)	
		if newPosition2:
			cel.append(newPosition1)
			cel.append(newPosition2)
		else:
			horizontal = 1
	else:
		horizontal = 1		
 	
	#testa posições a esquerda
	if horizontal == 1:
 		newPosition1 = esquerda(celulas,firstPosition, 1)
 		if newPosition1:
 			newPosition2 = esquerda(celulas,firstPosition, 2)
 			if newPosition2:
 				cel.append(newPosition1)
 				cel.append(newPosition2)
 			else:
 				vertical = 1	
 		else:
 			vertical = 1

 	#testa posições para baixo		
	if vertical == 1:
 		newPosition1 = down(celulas,firstPosition, 1)
 		if newPosition1:
 			newPosition2 = down(celulas,firstPosition, 2)
 			if newPosition2:
 				cel.append(newPosition1)
 				cel.append(newPosition2)
 			else:
 				vertical = 2	
 		else:
 			vertical = 2
	#Testa posições para cima
	if vertical == 2:
		newPosition1 = up(celulas,firstPosition, 1)
		if newPosition1:	
			newPosition2 = up(celulas,firstPosition, 2)
			if newPosition2:
				cel.append(newPosition1)
				cel.append(newPosition2)
			else:
				return -1
		else:
			return -1			
				
	return cel

def porta_aviao(celulas):
	'''
	celulas: celulas disponiveis para geração do porta avião
	preenche uma matriz com as coordenadas do porta avião e a retorna
	'''
	import random
	cel = []
	index = random.randint(0, len(celulas) - 1)
	#primeira posição gerada aleatoriamente, a partir dela gerar outras
	firstPosition = celulas[index]
	celulas.remove(firstPosition)
	horizontal = 0
	vertical = 0
	newPosition1 = direita(celulas,firstPosition, 1)
	if newPosition1:
		newPosition2 = direita(celulas,firstPosition, 2)
		if newPosition2:
			newPosition3 = direita(celulas,firstPosition, 3)
			if newPosition3:
				cel.append(newPosition1)
				cel.append(newPosition2)
				cel.append(newPosition3)
			else:
				horizontal = 1	
		else:
			horizontal = 1
	else:
		horizontal = 1		
 	
	if horizontal == 1:
		newPosition1 = esquerda(celulas,firstPosition, 1)
		if newPosition1:
			newPosition2 = esquerda(celulas,firstPosition, 2)
			if newPosition2:
				newPosition3 = esquerda(celulas,firstPosition, 3)
				if newPosition3:
					cel.append(newPosition1)
					cel.append(newPosition2)
					cel.append(newPosition3)
				else:
					vertical = 1	
			else:
				vertical = 1	
		else:
			vertical = 1
	

	if vertical == 1:
		newPosition1 = down(celulas,firstPosition, 1)
		if newPosition1:
			newPosition2 = down(celulas,firstPosition, 2)
			if newPosition2:
				newPosition3 = down(celulas,firstPosition, 3)
				if newPosition3:
					cel.append(newPosition1)
					cel.append(newPosition2)
					cel.append(newPosition3)
				else:
					vertical = 2		
			else:
				vertical = 2
		else:
			vertical = 2
				

	if vertical == 2:
		newPosition1 = up(celulas,firstPosition, 1)
		
		if newPosition1:
			newPosition2 = up(celulas,firstPosition, 2)
			if newPosition2:
				newPosition3 = up(celulas,firstPosition, 3)
				if newPosition3:
					cel.append(newPosition1)
					cel.append(newPosition2)
					cel.append(newPosition3)
				else:
					return -1
			else:
				return -1
		else:
			return -1
								

				
	cel.append(firstPosition)
	return cel	

def isAvailable(celulas, newPosition):
	'''
	celulas: celulas disponiveis para criação de um navio
	newPosition: uma nova posição
	retorna true/false dependendo de sua disponibilidade
	'''
	if newPosition in celulas:		
		celulas.remove(newPosition)
		return True
	return False
	
main()

