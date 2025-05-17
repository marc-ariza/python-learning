print("Please type in integer numbers. Type in 0 to finish.")

attempts = 0
suma = 0
positive = 0
negative = 0

while True:
    number = int(input("Number: "))
    attempts += 1
    suma += number

    if number == 0:
        attempts -= 1
        break
    elif number > 0:
        positive += 1
    else:
        negative += 1

mean = suma / attempts

print(f"Numbers typed in {attempts}")
print(f"The sum of the numbers is {suma}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")