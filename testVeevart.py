import random
#Diccionario de posiciones escalera
escaleras = {3: 11, 6: 17, 9: 18, 10: 12}
#Diccionario de posiciones serpiente
serpientes = {14: 4, 19: 8, 22: 20, 24: 16}
#Funcion para recibir el numero de jugadores
def cantidadJugadores():
    numJugadores = input("Digite el numero de jugadores que van a disputar la partida: ")
    dicJugadores = {}
    jugadores = range(int(numJugadores))
    posicionIni = 0
    for jugador in jugadores:
            dicJugadores[jugador+1] = posicionIni
    return dicJugadores
#Funcion para definir el tamaño del tablero
def tamanoTablero():
    tamHorizontal = input("Digite el ancho del tablero: ")
    tamVertical = input("Digite la altura del tablero: ")
    return int(tamHorizontal)*int(tamVertical)
#Funcion de juego
def juego(jugadoresDic, tamano):
    for i in jugadoresDic:
        dado = random.randint(1,6)
        print(f"Jugador {i} esta en la posicion: {jugadoresDic[i]}")
        print(f"Dado arroja: {dado}.")
        jugadoresDic[i] = jugadoresDic[i] + dado
        print(f"Jugador {i} ahora esta en la posicion: {jugadoresDic[i]}")
        if jugadoresDic[i] in escaleras:
            print("Has caido en una escalera")
            jugadoresDic[i] = escaleras[jugadoresDic[i]]
            print(f"Jugador {i} sube por escalera al cuadro: {jugadoresDic[i]}")
        elif jugadoresDic[i] in serpientes:
            print("Has caido en una serpiente")
            jugadoresDic[i] = serpientes[jugadoresDic[i]]
            print(f"Jugador {i} desciende al cuadro: {jugadoresDic[i]}.")
        else:
            print(f"Jugador {i} avanzó al cuadro: {jugadoresDic[i]}.")
        if jugadoresDic[i] == tamano:
            bandera = 2
            return bandera
        elif jugadoresDic[i] > tamano:
            devolverCuadros = jugadoresDic[i] - tamano
            jugadoresDic[i] = tamano - devolverCuadros
    print("\n")

def main():
    tamano = tamanoTablero()
    print(tamano)
    cantidad = cantidadJugadores()
    while True:
        jugadores = juego(cantidad, tamano)
        if jugadores == 2:
            print("Fin")
            break
main()
