#IMPORTAR NUMPY PARA GENERAR MATRIZ
#IMPORTAR RANDOM PARA GENERAR NUMEROS RANDOM PARA LOS ESPACIOS DE LA MAQUINA
#IMPORTAR COMANDOS DE SISTEMA

import numpy as np

import random as rd
import sys
import os

#MODIFICAR EL TAMANO DE CONSULTAS EN LOOP
sys.setrecursionlimit(9999)

#TF = TAMANO FILAS
#TC = TAMANO COLUMAS
tf = 3
tc = 3
#GENERACION DE TABLERO LLENADO CON ZEROS
#TABLERO=NUMPY.ZEROS((TAMANO FILAS,TAMANO COLUMNAS), DEFINIR TIPO=INTEGER)
tablero = np.array ([["#","#","#"],["#","#","#"],["#","#","#"]])

#def mensaje_despedida():
    #print("gracias por jugar")
    #return False


#VERIFICADOR DE GANADOR
def verifica_ganador(tablero,user,forma,cpu,cpu2):
    if tablero[0][0]==forma and tablero[0][1]==forma and tablero[0][2]==forma:
        print("\n\n\tGANASTE!!!!!  ", user )
        #mensaje_despedida()
        return False
    elif tablero[1][0]==forma and tablero[1][1]==forma and tablero[1][2]==forma:
        print("\n\n\tGANASTE!!!!!  ", user )
        #mensaje_despedida()
        return False
    elif tablero[2][0]==forma and tablero[2][1]==forma and tablero[2][2]==forma:
        print("\n\n\tGANASTE!!!!!  ", user )
        #mensaje_despedida()
        return False
    elif tablero[0][0]==forma and tablero[1][1]==forma and tablero[2][2]==forma:
        print("\n\n\tGANASTE!!!!!  ", user )
        #mensaje_despedida()
        return False
    elif tablero[0][2]==forma and tablero[1][1]==forma and tablero[2][0]==forma:
        print("\n\n\tGANASTE!!!!!  ", user )
        #mensaje_despedida()
        return False
    elif tablero[2][0]==forma and tablero[1][1]==forma and tablero[2][2]==forma:
        print("\n\n\tGANASTE!!!!!\n\n   ", user )
        #mensaje_despedida()
        return False
    elif tablero[0][0]==forma and tablero[1][0]==forma and tablero[2][0]==forma:
        print("\n\n\tGANASTE!!!!!\n\n   ", user )
        #mensaje_despedida()
        return False
    elif tablero[0][1]==forma and tablero[1][1]==forma and tablero[2][1]==forma:
        print("\n\n\tGANASTE!!!!!\n\n   ", user )
        #mensaje_despedida()
        return False
    elif tablero[0][2]==forma and tablero[1][2]==forma and tablero[2][2]==forma:
        print("\n\n\tGANASTE!!!!!\n\n   ", user )
        #mensaje_despedida()
        return False
    if tablero[0][0]==cpu2 and tablero[0][1]==cpu2 and tablero[0][2]==cpu2:
        print(tablero)
        print("\n\n\tGANASTE!!!!!  COMPUTADORA" )
        #mensaje_despedida()
        return False
    elif tablero[1][0]==cpu2 and tablero[1][1]==cpu2 and tablero[1][2]==cpu2:
        print(tablero)
        print("\n\n\tGANASTE!!!!!  COMPUTADORA  " )
        #mensaje_despedida()
        return False
    elif tablero[2][0]==cpu2 and tablero[2][1]==cpu2 and tablero[2][2]==cpu2:
        print(tablero)
        print("\n\n\tGANASTE!!!!!  COMPUTADORA  " )
        #mensaje_despedida()
        return False
    elif tablero[0][0]==cpu2 and tablero[1][1]==cpu2 and tablero[2][2]==cpu2:
        print(tablero)
        print("\n\n\tGANASTE!!!!!    COMPUTADORA" )
        #mensaje_despedida()
        return False
    elif tablero[0][2]==cpu2 and tablero[1][1]==cpu2 and tablero[2][0]==cpu2:
        print(tablero)
        print("\n\n\tGANASTE!!!!!     COMPUTADORA" )
        #mensaje_despedida()
        return False
    elif tablero[2][0]==cpu2 and tablero[1][1]==cpu2 and tablero[2][2]==cpu2:
        print(tablero)
        print("\n\n\tGANASTE!!!!!    COMPUTADORA " )
        #mensaje_despedida()
        return False
    elif tablero[0][0]==cpu2 and tablero[1][0]==cpu2 and tablero[2][0]==cpu2:
        print(tablero)
        print("\n\n\tGANASTE!!!!!    COMPUTADORA " )
        #mensaje_despedida()
        return False
    elif tablero[0][1]==cpu2 and tablero[1][1]==cpu2 and tablero[2][1]==cpu2:
        print(tablero)
        print("\n\n\tGANASTE!!  COMPUTADORA " )
        #mensaje_despedida()
        return False
    elif tablero[0][2]==cpu2 and tablero[1][2]==cpu2 and tablero[2][2]==cpu2:
        print(tablero)
        print("\n\n\tGANASTE!!!!!     COMPUTADORA " )
        #mensaje_despedida()
        return False
    else:
        return True

#GENERADOR DE POSISCIONAMIENTO RANDOM PARA LA MAQUINA
def genera_random(cpu2,cpu,forma):
    ciclo1=True
    while ciclo1==True:
        if forma.upper()=="X":
            fila=rd.randrange(0,3)
            columna=rd.randrange(0,3)
            if (tablero[fila][columna]!=forma) and (tablero[fila][columna]!=cpu) and (tablero[fila][columna]=="#") :
                tablero[fila][columna] = cpu
                print(tablero)
                return
            else: #tablero[fila,columna]==2 or tablero[fila,columna]==1:
                ciclo1=True
        elif forma.upper()=="O":
            print(tablero,"\n\n\n")
            fila=rd.randrange(0,3)
            columna=rd.randrange(0,3)
            if (tablero[fila][columna]!=forma) and (tablero[fila][columna]!=cpu2) and (tablero[fila][columna]=="#") :
                tablero[fila][columna] = cpu2
                print(tablero,"\n\n\n")
                return
            else: #tablero[fila,columna]==2 or tablero[fila,columna]==1:
                ciclo1=True
        else: #tablero[fila,columna]==2 or tablero[fila,columna]==1:
            ciclo1=True


#SELECCION DE COLUMNA Y DE FILAS USUARIO
def main_juego(forma,user,cpu,cpu2):#SE BORRO USER DEL DEF
    if verifica_ganador(tablero,user,forma,cpu,cpu2)==True:
        try:
            if forma.upper()=="X":
                fila = int(input('Primero Elije Fila:'))
                columna = int(input('Segundo Elije Columna:'))
                if (tablero[fila][columna]!=forma) and (tablero[fila][columna]!=cpu) and (tablero[fila][columna]=="#"):
                    tablero[fila][columna] = forma
                    genera_random(cpu2,cpu,forma)
                    verifica_ganador(tablero,user,forma,cpu,cpu2)
                    main_juego(forma,user,cpu,cpu2)
                    
                else:
                    print('espacio ocupado')
            elif forma.upper()=="O":
                genera_random(cpu2,cpu,forma)
                verifica_ganador(tablero,user,forma,cpu,cpu2)
                if verifica_ganador(tablero,user,forma,cpu,cpu2)==True:
                    fila = int(input('Primero Elije Fila:'))
                    columna = int(input('Segundo Elije Columna:'))
                    if (tablero[fila][columna]!=forma) and (tablero[fila][columna]!=cpu2) and (tablero[fila][columna]=="#"):
                        tablero[fila][columna] = forma
                        main_juego(forma,user,cpu,cpu2)
                    else:
                        print('espacio ocupado')
        except BaseException as error:
            print("error: ", error)

#MUESTRA DE DATOS DEL TABLERO Y SELECCION ACEPTAR COMENZAR
def menu():
    cpu="O"
    cpu2="X"
    flag=True
    if flag==True:
        #try:
            user=input("Ingrese su nombre: ")
            print("Selecciona Dificultad\nPresione X Para Comenzar primero \nPresione O Para Comenzar Segundo \nPresione S Para salir")
            forma=input("Seleccion: ")
            if forma.upper()=="X":
                print("el usuario ",user," usara forma ", forma.upper(),"\n\nbuena suerte\n\n")
                print("formato fila,columna\n")
                print("columna -> C0| C1| C2")
                print("Fila 0 -> 0,0|0,1|0,2\n          ---|---|---\nFila 1 -> 1,0|1,1|1,2\n          ---|---|---\nFila 2 -> 2,0|2,1|2,2")
                main_juego(forma,user,cpu,cpu2)#sumar un user
            if forma.upper()=="O":
                print("el usuario ",user," usara forma ", forma.upper(),"\n\nbuena suerte\n\n")
                print("formato fila,columna\n")
                print("columna -> C0| C1| C2")
                print("Fila 0 -> 0,0|0,1|0,2\n          ---|---|---\nFila 1 -> 1,0|1,1|1,2\n          ---|---|---\nFila 2 -> 2,0|2,1|2,2")
                main_juego(forma,user,cpu,cpu2)#sumar un user
            if forma.upper=="S":
                return
            if forma.upper()!="X" and forma.upper()!="O"and forma.upper()!="S":
                print("ahi dice presione 1, hay que tener un doctorado en harvard para leer instrucciones")
                menu()
        #except:
            else:
                return True
    else:
        return False

#MENU PRINCIPAL
if __name__=="__main__":
    print("\tJuego del NEKO NEKO\n")
    menu()
    print("GRACIAS POR JUGAR")
    os.system("pause")

#HECHO POR NESTOR CARVACHO