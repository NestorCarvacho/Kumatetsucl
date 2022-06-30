"""Crear una aplicacion que permita comprar pasajes de avion
el avion posee 6 columnas y un total de 30 filas
cada grupo de filas posee un valor particular
las 10 primeras filas poseen un valor de $25.000 el asiento
de la fila 11 al 24 poseen un valor de $15.000 el asiento
de la fila 25 al 30 poseen un valor de $10.000 el asieno

"""
import numpy as np
#matriz_avion=np.zeros((30,6),type(int))
n = 30
m = 6
asiento = np.zeros(shape=(n,m), dtype=int)
"""def revisar_asientos():
    num=1
    asiento=1
    ciclo=True
    while ciclo==True:
        for f in range(30):
            fila=str(num)
            for c in range(6):
                matriz_avion[f][c]=asiento
                fila=fila + '|' + str(matriz_avion[f][c])
                asiento=asiento+1
            print("fila",fila)
            num=num+1
            ciclo=False"""
def revisar_asientos():
        print('Mostrar_asientos')
        print(asiento)


def compra_boleto():
    costo=0
    valor=0
    ciclo=True
    while ciclo==True:
        p = int(input('fila:'))
        o = int(input('columna:'))
        for f in range(n):
            for c in range(m):
                if asiento == (p*o):
                    if asiento>=1 and asiento<=60:
                        costo=25000
                    if asiento>=61 and asiento<=144:
                        costo=15000
                    if asiento>144:
                        costo=10000
        if (asiento[p,o]==0):
            asiento[p,o] = 1
        else:
            print('asiento ocupado')

        valor=valor+costo
        print('El valor del asiento es :', costo)
        try:
            op2=int(input("desea agregar otro pasaje \n 1-SI/2-NO: "))
            if op2==1:
                ciclo=True
            if op2==2:
                print("Total a Pagar: ", valor)
                ciclo=False
        except:
            print("solo 1 o 2")


def menu():
    ciclo=True
    while ciclo==True:
        print("\t menu aerolinea nineleven \n1)Revisar asientos \n2)Comprar Boletos\n3)salir")
        try:
            op=int(input("Ingrese Opcion: "))
            if op==1:
                revisar_asientos()
            if op==2:
                compra_boleto()
            if op==3:
                ciclo=False
        except BaseException as error:
            print("ingrese opcion correcta por favor", error)

if __name__=="__main__":
    menu()
    print("Gracias por Preferir Aerolineas NinEleven")