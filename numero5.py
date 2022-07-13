## Escribir un algoritmo que lea cuatro números y, a continuación, escriba el mayor de los cuatro.
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num1 = int(input("ingrese el primer numero"))
num2 = int(input("ingrese el segundo numero"))
num3 = int(input("ingrese el tercer numero"))
num4 = int(input("ingrese el cuarto numero"))

if (num1 != num2 & num1 != num3 & num1 != num4 & num2 != num3 & num3 != num4):
    if (num1 > num2):
        if (num1 > num3):
            if (num1 > num4):
                print ("el mayor es " + str(num1))
            else:
                print("el mayor es " + str(num4))
        else:
            if (num3 > num4):
                print("el numero mayor es " + str(num3))
            else:
                print("el numero mayor es " + str(num4))
    else:
        if (num2> num3):
            if (num2 > num4):
                print("el numero mayor es " + str(num2))
            else:
                print("el numero mayor es " + str(num4))
        else:
            if(num3 > num4):
                print("el numero mayor es " + str(num3))
            else:
                print("el numero mayor es " + str(num4))
else:
    print("los numero no son diferentes") 