print('Bienvenido al tres en raya\n\nNormas:\nSi colocas el numero de un lugar ocupado, pasara al \nsiguiente jugador y no se colocara\nPara poner el numero de casilla primero columna y después \nfila\n')
p1=str(input('Introduzca el nombre del primer jugador: '))
p2=str(input('Introduzca el nombre del segundo jugador: '))
f=1
print()
n1=['?','?','?']
n2=['?','?','?']
n3=['?','?','?']
print(n1)
print(n2)
print(n3)
while f==1:
	print()
	p=int(input(p1+' introduzca XY: '))
	#X
	if p==11:
		if n1[0]==('?'):
			n1[0]=('x')
		else:
			print('\nSitio ocupado\n')
	elif p==21:
		if n1[1]==('?'):
			n1[1]=('x')
		else:
			print('\nSitio ocupado\n')
	elif p==31:
		if n1[2]==('?'):
			n1[2]=('x')
		else:
			print('\nSitio ocupado\n')
	elif p==12:
		if n2[0]==('?'):
			n2[0]=('x')
		else:
			print('\nSitio ocupado\n')
	elif p==22:
		if n2[1]==('?'):
			n2[1]=('x')
		else:
			print('\nSitio ocupado\n')
	elif p==32:
		if n2[2]==('?'):
			n2[2]=('x')
		else:
			print('\nSitio ocupado\n')
	elif p==13:
		if n3[0]==('?'):
			n3[0]=('x')
		else:
			print('\nSitio ocupado\n')
	elif p==23:
		if n3[1]==('?'):
			n3[1]=('x')
		else:
			print('\nSitio ocupado\n')
	elif p==33:
		if n3[2]==('?'):
			n3[2]=('x')
		else:
			print('\nSitio ocupado\n')
	
	print(n1)
	print(n2)
	print(n3)
	#Primera columna ganadora
	if n1[0]=='x':
		if n2[0]=='x':
			if n3[0]=='x':
				f=2
				print()
				print(p1+' ha ganado')
				input()
				break
	#Columna del medio ganadora
	if n1[1]=='x':
		if n2[1]=='x':
			if n3[1]=='x':
				f=2
				print()
				print(p1+' ha ganado')
				input()
				break
    #Columna del final ganadora
	if n1[2]=='x':
		if n2[2]=='x':
			if n3[2]=='x':
				f=2
				print()
				print(p1+' ha ganado')
				input()
				break
	#Primera fila ganadora
	if n1[0]=='x':
		if n1[1]=='x':
			if n1[2]=='x':
				f=2
				print()
				print(p1+' ha ganado')
				input()
				break
	#Segunda fila ganadora
	if n2[0]=='x':
		if n2[1]=='x':
			if n2[2]=='x':
				f=2
				print()
				print(p1+' ha ganado')
				input()
				break
	#Tercera fila ganadora
	if n3[0]=='x':
		if n3[1]=='x':
			if n3[2]=='x':
				f=2
				print()
				print(p1+' ha ganado')
				input()
				break
	#Diagonal arriba izquierda
	if n1[0]=='x':
		if n2[1]=='x':
			if n3[2]=='x':
				f=2
				print()
				print(p1+' ha ganado')
				input()
				break
	#Diagonal arriba derecha
	if n1[2]=='x':
		if n2[1]=='x':
			if n3[0]=='x':
				f=2
				print()
				print(p1+' ha ganado')
				input()
				break

	print()
	p=int(input(p2+' introduzca XY: '))
	#O
	if p==11:
		if n1[0]==('?'):
			n1[0]=('o')
		else:
			print('\nSitio ocupado\n')
	elif p==21:
		if n1[1]==('?'):
			n1[1]=('o')
		else:
			print('\nSitio ocupado\n')
	elif p==31:
		if n1[2]==('?'):
			n1[2]=('o')
		else:
			print('\nSitio ocupado\n')
	elif p==12:
		if n2[0]==('?'):
			n2[0]=('o')
		else:
			print('\nSitio ocupado\n')
	elif p==22:
		if n2[1]==('?'):
			n2[1]=('o')
		else:
			print('\nSitio ocupado\n')
	elif p==32:
		if n2[2]==('?'):
			n2[2]=('o')
		else:
			print('\nSitio ocupado\n')
	elif p==13:
		if n3[0]==('?'):
			n3[0]=('o')
		else:
			print('\nSitio ocupado\n')
	elif p==23:
		if n3[1]==('?'):
			n3[1]=('o')
		else:
			print('\nSitio ocupado\n')
	elif p==33:
		if n3[2]==('?'):
			n3[2]=('o')
		else:
			print('\nSitio ocupado\n')

	print(n1)
	print(n2)
	print(n3)

		#Primera columna ganadora
	if n1[0]=='o':
		if n2[0]=='o':
			if n3[0]=='o':
				f=2
				print()
				print(p2+' ha ganado')
				input()
				break
	#Columna del medio ganadora
	if n1[1]=='o':
		if n2[1]=='o':
			if n3[1]=='o':
				f=2
				print()
				print(p2+' ha ganado')
				input()
				break
    #Columna del final ganadora
	if n1[2]=='o':
		if n2[2]=='o':
			if n3[2]=='o':
				f=2
				print()
				print(p2+' ha ganado')
				input()
				break
	#Primera fila ganadora
	if n1[0]=='o':
		if n1[1]=='o':
			if n1[2]=='o':
				f=2
				print()
				print(p2+' ha ganado')
				input()
				break
	#Segunda fila ganadora
	if n2[0]=='o':
		if n2[1]=='o':
			if n2[2]=='o':
				f=2
				print()
				print(p2+' ha ganado')
				input()
				break
	#Tercera fila ganadora
	if n3[0]=='o':
		if n3[1]=='o':
			if n3[2]=='o':
				f=2
				print()
				print(p2+' ha ganado')
				input()
				break
	#Diagonal arriba izquierda
	if n1[0]=='o':
		if n2[1]=='o':
			if n3[2]=='o':
				f=2
				print()
				print(p2+' ha ganado')
				input()
				break
	#Diagonal arriba derecha
	if n1[2]=='o':
		if n2[1]=='o':
			if n3[0]=='o':
				f=2
				print()
				print(p2+' ha ganado')
				input()
				break