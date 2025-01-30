"""
Nombre: piedra_papel_tijera.py
Autor: Juliana Bolaños
Fecha: 30/01/2025
Descripción: Implementación del juego Piedra, Papel o Tijera con tres rondas
"""
import random

print("****************************************************************")
print("******** ¡Bienvenid@ al Juego Piedra, Papel o Tijera! **********")
print("****************************************************************\n")
print("1 - Para comenzar la partida \n2 - Para salir\n")

def juego():
    salida_maquina = " "
    salida_jugador = " "
    puntos_jugador = 0
    puntos_maquina = 0
    numero_rondas = 3
    contador_rondas = 0
    turno_jugador = True
    turno_maquina = False
    opciones = ["tijera", "papel", "piedra"]

    while numero_rondas > contador_rondas:
        print(f"\n********************* Empieza la Ronda {contador_rondas+1} ***********************\n")
        print(f"- Puntos maquina {puntos_maquina}.                       - Puntos jugador {puntos_jugador}. \n")

        while turno_jugador == True:
            salida_jugador = str(input("Elija (Piedra, Papel, Tijera): "))

            for opcion in opciones:
                if salida_jugador.lower() == opcion:
                    turno_jugador = False
                    turno_maquina = True

                    while turno_maquina == True:
                            salida_maquina = random.choice(opciones)
                            turno_maquina = False

                    puntos_jugador, puntos_maquina = verificar_jugada(salida_jugador.lower(), salida_maquina.lower(), puntos_jugador, puntos_maquina)

            if turno_jugador == True:
                print("Ingrese por favor una de las tres opciones validas\n")

        turno_jugador = True
        contador_rondas+=1
    print("\n***************************************************************")
    print("************************ Fin del Juego ************************")
    print("***************************************************************\n")
    print(f"* Puntos finales maquina {puntos_maquina}.         * Puntos finales jugador {puntos_jugador}. \n")

    if puntos_jugador > puntos_maquina:
        print("Felicidades, ganaste!!")
    elif puntos_maquina == puntos_jugador:
        print("Victoria para los dos, han empatado!")
    else:
        print("Perdiste, intentalo la proxima vez :(")

    print("\nBye")

def verificar_jugada(salida_jugador, salida_maquina, puntos_jugador, puntos_maquina):
    print("\n+ Informe de la Ronda")
    print(f"Tu jugada = {salida_jugador.capitalize()}              Jugada de la maquina = {salida_maquina.capitalize()}\n")
    
    if salida_jugador == salida_maquina:
        print("!Los dos han empatado!")
        puntos_jugador+=1
        puntos_maquina+=1

    elif (salida_jugador == "piedra" and salida_maquina == "tijera") or \
        (salida_jugador == "tijera" and salida_maquina == "papel") or \
        (salida_jugador == "papel" and salida_maquina == "piedra"):
        print("!El jugador ha ganado la ronda!")
        puntos_jugador+=1

    elif (salida_jugador == "tijera" and salida_maquina == "piedra") or \
        (salida_jugador == "papel" and salida_maquina == "tijera") or \
        (salida_jugador == "piedra" and salida_maquina == "papel"):
        print("!La maquina ha ganado la ronda!")
        puntos_maquina+=1
    else:
        print("Jugaba invalida")
    return puntos_jugador, puntos_maquina

entrar = False

while entrar == False:
    valor = int(input("Ingrese una opción: "))
    if valor == 1:
        entrar = True
        juego()
    elif valor == 2:
        entrar = True
        print("Saliendo...\n")
    else:
        print("Ingrese por favor un valor valido \n")
