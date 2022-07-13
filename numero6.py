# Diseñar un algoritmo para determinar si un número n es primo. (un número primo sólo es
#divisible por el mismo y por la unidad


numero1 = 0
contador = 0
i = 1

numero1 = int(input("ingrese un numero para saber si es primo"))


while i <= numero1:
    if numero1 % i == 0:
        contador = contador + 1
    i = i + 1
if (contador == 2):
    print("el numero es primo " + str(numero1))
else:
    print("el numero no es primo " + str(numero1))