
dia = int(input("ingrese un dia con el formato" + "xx"))
mes = int(input("ingrese un mes con el formato" + "xx"))
##año = int(input("ingrese un año con el formato" + "xxxx"))

if (dia == 31   ):
    if  (mes == 1) | (mes == 3) | (mes  == 5) | (mes == 7) | (mes == 8) | (mes == 10) | (mes == 12):
        dia2=1
        mes2=mes + 1
else:
    dia2=dia + 1
    mes2=mes
if (dia == 28):
    if (mes == 2):
        dia2 = 1
        mes2 = mes + 1


print("el dia siguiente es " + str(dia2))
print("el mes siguiente es " + str(mes2))
    

