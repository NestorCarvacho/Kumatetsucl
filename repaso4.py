#SIEMPRE INSTALAR NUMPY    ----->   CNTRL+Ñ
import numpy as np

#2 crear matriz
arreglo = np.array([2,3,5])

#cargar valor en la matriz
matriz= np.zeros((3,3))

#recorrer
matriz[0][0]=int(input('ingrese Numero: '))

for f in range(3):
    fila=''
    for c in range(3):
        fila=fila + '|' + str(matriz[f][c])
    print(fila)


