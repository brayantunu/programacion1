num1 = 0
num1 = int(input("ingrese un numero impar para hacer la suma y la serie"))
suma = 0
while (num1 <= 99):
    print(num1)
    suma = suma + num1
    num1 = num1 + 3

print("la suma de la serie de numeros imperes es " + str(suma))