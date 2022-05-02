import random
#Diccionario de posiciones escalera
escaleras = {3: 11, 6: 17, 9: 18, 10: 12}
print(escaleras)
#Diccionario de posiciones serpiente
serpientes = {14: 4, 19: 8, 22: 20, 24: 16}
print(serpientes)
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
#Funcion de juego que manejara los turnos de los jugadores
def juego(jugadoresDic, tamano):
    # Ciclo de manejo de turnos por medio de un diccionario y su key
    for i in jugadoresDic:
        dado = random.randint(1,6)
        print(f"Jugador {i} esta en la posicion: {jugadoresDic[i]}")
        print(f"Dado arroja: {dado}.")
        jugadoresDic[i] = jugadoresDic[i] + dado
        print(f"Jugador {i} ahora esta en la posicion: {jugadoresDic[i]}")
        # Se evalua si el jugador ha caido en una escalera
        if jugadoresDic[i] in escaleras:
            print("Has caido en una escalera")
            jugadoresDic[i] = escaleras[jugadoresDic[i]]
            print(f"Jugador {i} sube por escalera al cuadro: {jugadoresDic[i]}")
        # Se evalua si el jugador ha caido en una serpiente
        elif jugadoresDic[i] in serpientes:
            print("Has caido en una serpiente")
            jugadoresDic[i] = serpientes[jugadoresDic[i]]
            print(f"Jugador {i} desciende al cuadro: {jugadoresDic[i]}.")
        else:
            print(f"Jugador {i} avanzó al cuadro: {jugadoresDic[i]}.")
        # Se evalua si el jugador ha caido el cuadro ganador
        # Si cae en cuadro ganador se activa la bandera y el jugo termina con un ganador
        if jugadoresDic[i] == tamano:
            bandera = 1
            return bandera
        # Se evalua si el jugador ha caido en un cuadro que supera al ganador
        # Si supera al cuadro ganador se resta los cuadros extras con su posicion
        elif jugadoresDic[i] > tamano:
            devolverCuadros = jugadoresDic[i] - tamano
            jugadoresDic[i] = tamano - devolverCuadros
            print(f"Jugador {i} se paso por {devolverCuadros} cuadros. Volvera al cuadro {jugadoresDic[i]}")
            # Se evalua de nuevo si el jugador ha caido en una escalera debido a que supero el cuadro ganador
            if jugadoresDic[i] in escaleras:
                print("Has caido en una escalera")
                jugadoresDic[i] = escaleras[jugadoresDic[i]]
                print(f"Jugador {i} sube por escalera al cuadro: {jugadoresDic[i]}")
            # Se evalua de nuevo si el jugador ha caido en una serpiente debido a que supero el cuadro ganador
            elif jugadoresDic[i] in serpientes:
                print("Has caido en una serpiente")
                jugadoresDic[i] = serpientes[jugadoresDic[i]]
                print(f"Jugador {i} desciende al cuadro: {jugadoresDic[i]}.")
    print("\n")

def main():
    tamano = tamanoTablero()
    print(tamano)
    cantidad = cantidadJugadores()
    while True:
        jugadores = juego(cantidad, tamano)
        if jugadores == 1:
            print("Fin")
            break
main()
