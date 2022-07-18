dia = int(input("ingrese un dia con el formato" + " xx : "))
mes = int(input("ingrese un mes con el formato" + " xx : "))
alo = int(input("ingrese un año con el formato" + " xxxx : "))

if (dia == 31 and  (mes == 1) | (mes == 3) | (mes  == 5) | (mes == 7) | (mes == 8) | (mes == 10) | (mes == 12)): #comparamos los meses que tienen 31 dias y hace cambio de mes iniciando dia 1
    
    dia = 1
    mes = mes + 1
elif (dia == 30 and  (mes == 1) | (mes == 3) | (mes  == 5) | (mes == 7) | (mes == 8) | (mes == 10) | (mes == 12)): #comparamos los meses que tienen 31 dias y hace cambio de mes iniciando dia 1
elif (dia == 30 and  (mes == 4) | (mes == 6) | (mes  == 9) | (mes == 11) ): #comparamos los meses que tienen 31 dias y hace cambio de mes iniciando dia 1
elif (dia == 30 and  (mes == 4) | (mes == 6) | (mes  == 9) | (mes == 11) ): #comparamos los meses que tienen 31 dias y hace cambio de mes iniciando dia 1
elif (dia == 30 and  (mes == 4) | (mes == 6) | (mes  == 9) | (mes == 11) ): #comparamos los meses que tienen 31 dias y hace cambio de mes iniciando dia 1
elif (dia == 30 and  (mes == 4) | (mes == 6) | (mes  == 9) | (mes == 11) ): #comparamos los meses que tienen 31 dias y hace camio de mes iniciando dia 1
elif (dia == 30 and  (mes == 4) | (mes == 6) | (mes  == 9) | (mes == 11) ): #comparamos los meses que tienen 31 dias y hace cambio de mes iniciando dia 1
else:
    if (dia  == 30 and  (mes == 4) ):
        dia = 1
        mes = mes + 1
         
    dia = dia + 1
        
    if (mes == 2 and (dia == 29 or (dia == 28 and (alo % 4 != 0 )))): # evaluar si un año es bisiesto 
        
        dia = 1
        mes = mes + 1
    else:
        dia = dia + 1
    
    if (mes == 13): # evaluar si se digito el mes de diciembre 12
            dia = 1
            mes = 1
            alo + 1  

                
    
print("el dia siguiente es " + str(dia))
print("el mes siguiente es " + str(mes))
print("el año en que se encuentra es " + str(alo))
  

# if (dia >= 31):
#   print("el numero ingresado no es permitido vuelve e intenta")
#   dia = int(input("ingrese un dia con el formato" + " xx : "))
#   mes = int(input("ingrese un mes con el formato" + " xx : "))
#   alo = int(input("ingrese un año con el formato" + " xxxx : "))

#if (dia > 31):# aqui cuando ingresemos un numero mayor el sistema lo rechaza
 #   print("la fecha esta fuera de los limites")
#else: