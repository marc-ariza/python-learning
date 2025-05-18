limit = int(input("Limit: "))
suma = 0
lastnumber = 0

while lastnumber < limit:
    suma += 1
    lastnumber += suma
print(lastnumber)

