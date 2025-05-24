word = input("Please type in a string: ")
amount = int(input("Please type in an amount: "))
row = ""

while amount > 0:
    row += word
    amount -= 1

print(row)