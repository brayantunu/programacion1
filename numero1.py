from asyncio import subprocess
from calendar import c
from concurrent.futures import process
from importlib import import_module
from re import sub


    
c = input("ingrese una palabra")

for indice in c:
         contador = contador + 1


for i in c:
    if i == c[contador - 1]:
     contador = contador - 1
    if contador == 0:
            print("la palabra " + c + " es palindrome")
    else:
            print("la palabra " + c + " no es palidrome")

        
