

from re import L
from tkinter import N
from unittest import result
n = input("ingrese cualquier frase : ")

print("hola : " + n)

print(((3+2) / (2*5))**2)


horas = float(input("ingrese las horas de trabajo :"))
coste = float(input("ingrese el coste de la hora :"))

pago = horas*coste

print("tu pago es : " , pago)

n = int(input("ingrese un numero : "))

resultado = n * (n + 1) / 2

print("la suma de los primeros numero enteros desde 1 hasta " + str(n))
print(str(resultado))


peso = float(input("ingresel el peso corporal"))
metros = float(input("ingrese la altura"))

s = peso / (metros)**2

print("tu indice de masa coporal es : " + str(s))

l = int(input("ingrese un numero : "))
m = int(input("ingrese otro numero : "))

if (l < m ):
    print("el numero del divisor es muy grande")
else:
    r = (l / m)
    p = (l % m)

    print("el numero divisor " , l , " y el divisor " , m , "el resulatado es : " , str( r ) , str( p ))