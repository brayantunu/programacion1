n1 = int(input("ingrese el primer numero"))
n2 = int(input("ingrese el segundo numero"))
n3 = int(input("ingrese el tercer numero"))

if (n1 != n2 and n1 != n3 and n2 != n3):
    if (n1 > n2):
        if (n1 > n3):
            print("el numero central es " , n1)
        else:
            print("el numero central es " , n3)
    else:
        if (n2 > n3)        :
            print("el numero central es " , n2)
        else:
            print("el numero central es " , n3)

else:
    print("los numeros se repiten vuelve eh intenta")