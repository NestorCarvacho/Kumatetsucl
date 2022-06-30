#IMPORTAR NUMPY PARA GENERAR MATRIZ
#IMPORTAR RANDOM PARA GENERAR NUMEROS RANDOM PARA LOS ESPACIOS DE LA MAQUINA
#IMPORTAR COMANDOS DE SISTEMA

import numpy as np
import random as rd
import sys
import os

ciclo_jugada = True
ciclo_juego = True
#MODIFICAR EL TAMANO DE CONSULTAS EN LOOP
sys.setrecursionlimit(9999)

#Generacion de tablero en blanco
tablero = np.array ([["7","8","9"],["4","5","6"],["1","2","3"]])


def verifica_ganador(tablero,ficha):
    if tablero[0][0]==ficha and tablero[0][1]==ficha and tablero[0][2]==ficha:
        print_tablero()
        print("\n\n\tGANASTE!!!!!  ")
        print("GRACIAS POR JUGAR")
        return False
    elif tablero[1][0]==ficha and tablero[1][1]==ficha and tablero[1][2]==ficha:
        print_tablero()
        print("\n\n\tGANASTE!!!!!  ")
        print("GRACIAS POR JUGAR")
        return False
    elif tablero[2][0]==ficha and tablero[2][1]==ficha and tablero[2][2]==ficha:
        print_tablero()
        print("\n\n\tGANASTE!!!!!  ")
        return False
    elif tablero[0][0]==ficha and tablero[1][1]==ficha and tablero[2][2]==ficha:
        print_tablero()
        print("\n\n\tGANASTE!!!!!\n\n   ")
        return False
    elif tablero[0][2]==ficha and tablero[2][2]==ficha and tablero[2][0]==ficha:
        print_tablero()
        print("\n\n\tGANASTE!!!!!\n\n   ")
        return False
    elif tablero[2][0]==ficha and tablero[2][1]==ficha and tablero[2][2]==ficha:
        print_tablero()
        print("\n\n\tGANASTE!!!!!\n\n   ")
        return False
    elif tablero[0][0]==ficha and tablero[1][0]==ficha and tablero[2][0]==ficha:
        print_tablero()
        print("\n\n\tGANASTE!!!!!\n\n   ")
        return False
    elif tablero[0][1]==ficha and tablero[1][1]==ficha and tablero[2][1]==ficha:
        print_tablero()
        print("\n\n\tGANASTE!!!!!\n\n   ")
        return False
    elif tablero[0][2]==ficha and tablero[1][2]==ficha and tablero[2][2]==ficha:
        print_tablero()
        print("\n\n\tGANASTE!!!!!\n\n   ")
        return False
    else:
        return True


def genera_random(ficha, ficha2):
    cicloverif=verifica_ganador(tablero,ficha)
    while cicloverif==True:
        cpuf=rd.randrange(0,3)
        cpuc=rd.randrange(0,3)
        if (tablero[cpuf][cpuc]!=ficha2 and tablero[cpuf][cpuc]!=ficha):
            tablero[cpuf][cpuc] = ficha2
            return
        else:
            cicloverif=True

#Ingreso de fichas, mediante la conversión de numeros a coordenadas del arreglo
def ingreso_ficha(ficha, ficha2):
    os.system("cls")
    ciclo_jugada = verifica_ganador(tablero,ficha)
    while ciclo_jugada == True:
        try:
            print_tablero()
            jugada = int(input("Ingrese el numero de la casilla que desee: "))
            if jugada == 1:
                if tablero[2][0] != ficha and tablero[2][0] != ficha2:
                    tablero[2][0] = ficha
                    genera_random(ficha, ficha2)
                    verifica_ganador(tablero,ficha)
                else:
                    print("\ncasilla ocupada\n")
            elif jugada == 2:
                if tablero[2][1] != ficha and tablero[2][1] != ficha2:
                    tablero[2][1] = ficha
                    verifica_ganador(tablero,ficha)
                    genera_random(ficha, ficha2)
                else:
                    print("\ncasilla ocupada\n")
            elif jugada == 3:
                if tablero[2][2] != ficha and tablero[2][2] != ficha2:
                    tablero[2][2] = ficha
                    verifica_ganador(tablero,ficha)
                    genera_random(ficha, ficha2)
                else:
                    print("\ncasilla ocupada\n")
            elif jugada == 4:
                if tablero[1][0] != ficha and tablero[1][0] != ficha2:
                    tablero[1][0] = ficha
                    verifica_ganador(tablero,ficha)
                    genera_random(ficha, ficha2)
                else:
                    print("\ncasilla ocupada\n")
            elif jugada == 5:
                if tablero[1][1] != ficha and tablero[1][1] != ficha2:
                    tablero[1][1] = ficha
                    verifica_ganador(tablero,ficha)
                    genera_random(ficha, ficha2)
                else:
                    print("\ncasilla ocupada\n")
            elif jugada == 6:
                if tablero[1][2] != ficha and tablero[1][2] != ficha2:
                    tablero[1][2] = ficha
                    verifica_ganador(tablero,ficha)
                    genera_random(ficha, ficha2)
                else:
                    print("\ncasilla ocupada\n")
            elif jugada == 7:
                if tablero[0][0] != ficha and tablero[0][0] != ficha2:
                    tablero[0][0] = ficha
                    verifica_ganador(tablero,ficha)
                    genera_random(ficha, ficha2)
                else:
                    print("\ncasilla ocupada\n")
            elif jugada == 8:
                if tablero[0][1] != ficha and tablero[0][1] != ficha2:
                    tablero[0][1] = ficha
                    verifica_ganador(tablero,ficha)
                    genera_random(ficha, ficha2)
                else:
                    print("\ncasilla ocupada\n")
            elif jugada == 9:
                if tablero[0][2] != ficha and tablero[0][2] != ficha2:
                    tablero[0][2] = ficha
                    verifica_ganador(tablero,ficha)
                    genera_random(ficha, ficha2)
                else:
                    print("\ncasilla ocupada\n")
            else:
                print("casilla ocupada")
                ciclo_jugada = True
        except:
            print("Ingrese un numero valido")
            os.system("pause")



def print_tablero():
    print(f"\t {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]}")
    print(f"\t---+---+---")
    print(f"\t {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]}")
    print(f"\t---+---+---")
    print(f"\t {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]}")

def juego(ficha, ficha2):
    ciclo_juego = ingreso_ficha(ficha, ficha2)
    while ciclo_juego == True:
        os.system("cls")
        print(f"Turno de: {ficha}")
        print_tablero()
        ingreso_ficha(ficha, ficha2)

    os.system("pause")

#Introducción del juego
def introduccion(ficha, ficha2):
    os.system("cls")
    print("\t Introducción del juego")
    print("El tablero se encuentra ordenado de la siguiente forma:")
    print_tablero()
    print("Para colocar una ficha, ingrese el número de la casilla que desee")
    print("Puedes hacer cuenta que es como el teclado numerico")
    if ficha == "X":
        print("Como seleccionaste Cruz, comienza primero")
    elif ficha == "O":
        print("Como seleccionaste Circulo, comienza segundo")
    os.system("pause")
    juego(ficha, ficha2)


#Menú de inicio
def menu():
    ciclo = True
    while ciclo == True:
        try:
            os.system("cls")
            print("\t Bienvenido al juego del gato")
            print("Para jugar, ingrese el numero de la opcion que desee (Cruz juega primero, circulo segundo)")
            print("1) Cruz")
            print("2) Circulo")
            print("3) Salir")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                ficha = "X"
                ficha2 = "O"
                introduccion(ficha, ficha2)
            elif opcion == 2:
                ficha = "O"
                ficha2 = "X"
                introduccion(ficha, ficha2)
            elif opcion == 3:
                ciclo = False
                print("Gracias por jugar")
                sys.exit()
            else:
                print("Opcion no valida")
                os.system("pause")
        except BaseException as error:
            print("Error, ingrese un numero", error)
            os.system("pause")
            

if __name__ == "__main__":
    menu()
