def promedio(n1,n2,n3):
    suma =n1+n2+n3
    promedio=round(suma/3,2)
    return promedio

def validar_nota():
    ciclo=True
    while (ciclo==True):
        try:
            nota=float(input('ingrese Nota: '))
            if nota>=1 and nota<=7:
                return nota
            else:
                print('\t ¡No sea pillo!, la nota es de 1 a 7')
        except:
            print('\t ¡Ingrese Solo Numeros!')

def validar_respuesta():
    ciclo=True
    while(ciclo==True):
        resp=input('desea generar otro promedio: (S/N): ')
        if resp.upper()=='S' or resp.upper()=='N':
            return resp.upper()
        else:
            print('\t ¡Solamente S o N!')

ciclo=True
while (ciclo==True):
    n1 = validar_nota()
    n2 = validar_nota()
    n3 = validar_nota()
    print('\n el promedio es: ', promedio(n1,n2,n3))
    resp=validar_respuesta()
    if resp=='N':
        ciclo=False