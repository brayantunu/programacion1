from operator import mod


producto = 1
x = 20
suma = 0
for x in range(20,400 + 1):
    if x % 2 == 0 :
        suma = suma + x
        producto = producto * x

    print("la suma es " + str(suma))
    print("el producto es " + str(producto))