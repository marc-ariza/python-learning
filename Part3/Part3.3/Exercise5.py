number = int(input("Please type in an number: "))
index = 1
start_number = number

while start_number > 0:
    print(index)
    if index == number:
        break
    print(number)
    index += 1
    number -= 1
    start_number -= 2



