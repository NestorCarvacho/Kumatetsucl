#crear aplicaion que permita sacar el promedio de 3 notas

n1=float(input('ingrese primera nota: '))
n2=float(input('ingrese segunda nota: '))
n3=float(input('ingrese tercera nota: '))

suma=n1+n2+n3
promedio=round(suma/3,2)

print('su promedio es : ', promedio)