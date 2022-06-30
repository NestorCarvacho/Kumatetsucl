import numpy as np
import random as rn
import os

tablero = np.array([['1','2','3'],['4','5','6'],['7','8','9']])
print("juego gato")
jugadas=0
switch=True
while switch:
    jugador=input("Seleccione X - O: ").upper()
    if jugador=='X':
        jugador='X'
        cpu='O'
        switch=False
    elif jugador=='O':
        jugador='O'
        cpu='X'
        switch=False
    else:
        print("Opcion incorrecta")


def tablero_gato(tablero):
    for f in range(3):
        fila= ''
        for c in range(3):
            fila= fila + '  |  ' + str(tablero[f][c])
        print(f"\t{fila+'  |  '}")
        print(f"\t  ------+-----+-----+")


def ganador_juego(tablero,jugador,cpu):
    if tablero[0][0]==cpu and tablero[0][1]==cpu and tablero[0][2]==cpu:
        print(f"Ganador: {cpu}")
        return False
    if tablero[1][0]==cpu and tablero[1][1]==cpu and tablero[1][2]==cpu:
        print(f"Ganador: {cpu}")
        return False
    if tablero[2][0]==cpu and tablero[2][1]==cpu and tablero[2][2]==cpu:
        print(f"Ganador: {cpu}")
        return False
    if tablero[0][0]==cpu and tablero[1][0]==cpu and tablero[2][0]==cpu:
        print(f"Ganador: {cpu}")
        return False
    if tablero[0][1]==cpu and tablero[1][1]==cpu and tablero[2][1]==cpu:
        print(f"Ganador: {cpu}")
        return False
    if tablero[0][2]==cpu and tablero[1][2]==cpu and tablero[2][2]==cpu:
        print(f"Ganador: {cpu}")
        return False
    if tablero[0][0]==cpu and tablero[1][1]==cpu and tablero[2][2]==cpu:
        print(f"Ganador: {cpu}")
        return False
    if tablero[0][2]==cpu and tablero[1][1]==cpu and tablero[2][0]==cpu:
        print(f"Ganador: {cpu}")
        return False
    if tablero[0][0]==jugador and tablero[0][1]==jugador and tablero[0][2]==jugador:
        print(f"Ganador: {jugador}")
        return False
    if tablero[0][0]==jugador and tablero[0][1]==jugador and tablero[0][2]==jugador:
        print(f"Ganador: {jugador}")
        return False
    if tablero[2][0]==jugador and tablero[2][1]==jugador and tablero[2][2]==jugador:
        print(f"Ganador: {jugador}")
    if tablero[0][0]==jugador and tablero[1][0]==jugador and tablero[2][0]==jugador:
        print(f"Ganador: {cpu}")
        return False
    if tablero[0][1]==jugador and tablero[1][1]==jugador and tablero[2][1]==jugador:
        print(f"Ganador: {jugador}")
        return False
    if tablero[0][2]==jugador and tablero[1][2]==jugador and tablero[2][2]==jugador:
        print(f"Ganador: {jugador}")
        return False
    if tablero[0][0]==jugador and tablero[1][1]==jugador and tablero[2][2]==jugador:
        print(f"Ganador: {jugador}")
        return False
    if tablero[0][2]==jugador and tablero[1][1]==jugador and tablero[2][0]==jugador:
        print(f"Ganador: {jugador}")
        return False
    else:
        return True
    


def opcion_jugador(tablero,jugador,jugadas):
    jugada=input("Ingrese jugada 1-9: ")
    if jugada=='1':
        if tablero[0][0]!='X' and tablero[0][0]!='O':
            tablero[0][0]= jugador
            jugada_aleatoria(tablero,cpu)
            jugadas=jugadas+1
        else:
            print("Casilla ya jugada")
    if jugada=='2':
        if tablero[0][1]!='X' and tablero[0][1]!='O':
            tablero[0][1]= jugador
            jugada_aleatoria(tablero,cpu)
            jugadas=jugadas+1
        else:
            print("Casilla ya jugada")
    if jugada=='3':
        if tablero[0][2]!='X' and tablero[0][2]!='O':
            tablero[0][2]= jugador
            jugada_aleatoria(tablero,cpu)
            jugadas=jugadas+1
        else:
            print("Casilla ya jugada")
    if jugada=='4':
        if tablero[1][0]!='X' and tablero[1][0]!='O':
            tablero[1][0]= jugador
            jugada_aleatoria(tablero,cpu)
            jugadas=jugadas+1
        else:
            print("Casilla ya jugada")
    if jugada=='5':
        if tablero[1][1]!='X' and tablero[1][1]!='O':
            tablero[1][1]= jugador
            jugada_aleatoria(tablero,cpu)
            jugadas=jugadas+1
        else:
            print("Casilla ya jugada")
    if jugada=='6':
        if tablero[1][2]!='X' and tablero[1][2]!='O':
            tablero[1][2]= jugador
            jugada_aleatoria(tablero,cpu)
            jugadas=jugadas+1
        else:
            print("Casilla ya jugada")
    if jugada=='7':
        if tablero[2][0]!='X' and tablero[2][0]!='O':
            tablero[2][0]= jugador
            jugada_aleatoria(tablero,cpu)
            jugadas=jugadas+1
        else:
            print("Casilla ya jugada")
    if jugada=='8':
        if tablero[2][1]!='X' and tablero[2][1]!='O':
            tablero[2][1]= jugador
            jugada_aleatoria(tablero,cpu)
            jugadas=jugadas+1
        else:
            print("Casilla ya jugada")
    if jugada=='9':
        if tablero[2][2]!='X' and tablero[2][2]!='O':
            tablero[2][2]= jugador
            jugada_aleatoria(tablero,cpu)
            jugadas=jugadas+1
        else:
            print("Casilla ya jugada")

def jugada_aleatoria(tablero,cpu):
    switch=True
    while switch==True:
        columna = rn.randint(0,2)
        fila  = rn.randint(0,2)
        if tablero[fila][columna]!="X" and tablero[fila][columna]!="O":
            tablero[fila][columna]=cpu
            switch=False

os.system("cls")
print("JUEGO GATO, EXPLICACIONES: PARAR JUGAR USTED TENDR QUE ELEGIR UNA CASILLA LA CUAL EST LISTADA DEL 1 AL 9. ")
tablero_gato(tablero)
switch=True
opcion=0  
while ganador_juego(tablero,jugador,cpu)==True:
    opcion_jugador(tablero,jugador,jugadas)
    tablero_gato(tablero)
    print(jugadas)
    if jugadas==9:
        jugadas=jugadas+1
        
            

'''opcion=int(input("Desea jugar nuevamente? 1) Si 2) No "))
if opcion==2:
    print("Gracias por jugar. creado por Ernesto Baeza, Felipe Arcos, Nicolas Muñoz")
    switch=False'''
