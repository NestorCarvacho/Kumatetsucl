def promedio(n1,n2,n3):
    suma =n1+n2+n3
    promedio=round(suma/3,2)
    return promedio


n1 = float(input('ingrese nota 1: '))
n2 = float(input('ingrese nota 2: '))
n3 = float(input('ingrese nota 3: '))
print('el promedio es: ',promedio(n1,n2,n3))
