from ctypes.wintypes import CHAR
import string


minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase
otro = 

letra = input("ingrese una letra")

def codigo(letra):
    if letra in minusculas:
        return minusculas.index(letra) + 97
    if letra in mayusculas:
        return mayusculas.index(letra) + 65

print(codigo (letra))