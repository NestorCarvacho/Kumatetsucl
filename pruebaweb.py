# ICM00794-Fundamentos de Computacion - FCNM-ESPOL
import numpy as np

# Genera la sala
n = 30
m = 6
asiento = np.zeros(shape=(n,m), dtype=int)

opcion = '0'
while not(opcion=='5'):
    print(' 1. Vender Boletos')
    print(' 2._Mostrar_asientos')
    print(' 3. Contar vendidos')
    print(' 4. Buscar libre')
    print(' 5. Salir ')

    opcion = input('cual opcion: ')

    if (opcion=='1'):
        print('Vender Boletos')
        fila = int(input('fila:'))
        columna = int(input('columna:'))
        if (asiento[fila,columna]==0):
            asiento[fila,columna] = 1
        else:
            print('asiento ocupado')

        
    if (opcion=='2'):
        print('Mostrar_asientos')
        print(asiento)
        
    if (opcion=='3'):
        print('Contar vendidos')
        contar = 0
        for fila in range(0,n,1):
            for columna in range(0,m,1):
                contar = contar+asiento[fila,columna]
        print(contar)
        
    if (opcion=='4'):
        print('Buscar libre')
        
    if (opcion=='5'):
        print('Salir')