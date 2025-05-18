limit = int(input("Limit: "))
suma = 0
lastnumber = 0
words = ""

while lastnumber < limit:
    suma += 1
    lastnumber += suma

    if lastnumber < limit:
        words += f"{suma} + "
    if lastnumber >= limit:
        words += f"{suma}"

print(f"The consecutive sum: {words} = {lastnumber}")

