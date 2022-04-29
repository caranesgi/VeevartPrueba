import random

#Posicion jugador
jugador1 = 0

#Diccionario de posiciones escalera
escalera = {
	3: 11,
	6: 17,
	9: 18,
	10: 12
}

#Diccionario de posiciones serpiente
serpiente = {
	14: 4,
	19: 8,
	22: 20,
	24: 16,
}

#Funcion principal
def jugada(posicion):
	dado = random.randint(1,6)
	print("Dado arroja: {}.".format(dado))
	#print(f"Dado arroja: {dado}")
	posicion = posicion + dado
	if posicion in escalera:
		print("Has caido en una escalera")
		posicion = escalera[posicion]
		print("Jugador sube por escalera al cuadro: {}.".format(posicion))
		#print(f"Jugador sube por escalera al cuadro: {posicion}")
	elif posicion in serpiente:
		print("Has caido en una serpiente")
		posicion = serpiente[posicion]
		print("Jugador desciende al cuadro: {}.".format(posicion))
		#print(f"Jugador desciende al cuadro: {posicion}")
	else:
		print("Jugador avanza a cuadro: {}.".format(posicion))
		#print(f"Jugador avanza a cuadro {posicion}")
	print("\n")
	return posicion

while True:
	jugador1 = jugada(jugador1)
	if jugador1 >= 25:
		print("Game over")
		break



