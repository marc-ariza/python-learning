input_string = input("Please type in a string: ")
lenght = len(input_string)
index = -1

while index >= -abs(lenght):
    print(input_string[index])
    index -= 1

