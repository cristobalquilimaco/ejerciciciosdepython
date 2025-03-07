import random

#Creea un juego de piedra papel o tijera

"""Definir las opciones y reglas del juego:

Piedra vence a tijera
Tijera vence a papel
Papel vence a piedra
Implementar la lógica del juego:

Pedir al jugador que elija entre piedra, papel o tijera.
Generar una elección aleatoria para la computadora.
Comparar las elecciones para determinar el ganador.
Mostrar el resultado y preguntar al jugador si desea jugar de nuevo."""

def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]

    while True:
        print("Bienvenido al juego, priedra papel o tijera")
        print("Por favor ingresa una opcion")
        print("Piedra")
        print("Papel")
        print("Tijera")
        print("4 para salir")
        
        jugador = input("Ingresa tu opcion-->")
        jugador.lower()
        print(jugador)
        computer = random.choice(opciones)
        computer.lower()
        print(computer)

        if jugador == "4":
            print("Gracias por jugar ")
            break
        if jugador == computer:
            print("Empate")
        elif jugador == "Piedra" or computer == "Tijera":
            print(f"Felicidades Ganaste! --> computer eligio {computer}")
            break
        elif jugador == "Papel" or computer == "Piedra":
            print(f"Felicidades Ganaste! --> computer eligio {computer}")
            break
        elif jugador == "Tijera" or computer == "Papel":
            print(f"Felicidades Ganaste! --> computer eligio {computer}")
            break
        else:
            print(f"Perdiste --> computer eligio {computer}\n")

jugar_piedra_papel_tijera()