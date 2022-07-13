impar = 0
par = 0
n = 0
i = 1
i = i + 1



for i in 1:
    n = int(input("ingrese los numeros " + 1))
    if (n % 2 == 0):
        par = par + n
    else:
        impar = impar + n

print("suma de los numeros pares es " + str(par))
print("la suma de los impares es" + str(impar))
