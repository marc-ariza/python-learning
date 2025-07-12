number = int(input("Please type in an number: "))
start = 0
start_pair = -1
number_start = number

while number > 0:
    start += 2
    if start <= number_start:
        print(start)
    
    start_pair += 2
    if start_pair <= number_start:
        print(start_pair)
    number -= 2

