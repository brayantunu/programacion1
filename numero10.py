num1 = int(input("pon un numero para obtener los muultiplos"))
p = int(input("asta que limite deseas que termine"))
i = 1
multiplos = num1

print("los multiplos de ", num1)
while (multiplos < p):
    print("son " , multiplos)
    i = i + 1
    multiplos = num1 * i

