mcd = 0
num1 = int(input("ingrese el primer numero"))
num2 = int(input("ingrese otro numero"))


if (num1 > num2):
        contiene = num2
else:
        contiene = num1
for mcd in range(1, contiene + 1):
        if ((num1 % mcd == 0) and (num2 % mcd == 0)):
            resultado = mcd

print("el maximo comun divisor de " + str(num1) + " y " + str(num2) + " es " + str(resultado))
