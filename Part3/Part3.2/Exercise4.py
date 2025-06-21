text = input("Please type in a string: ")
letter1 = text[1]
letter2 = text[-2]

if letter1 == letter2:
    print(f"The second and the second to last characters are {letter1}")
else:
    print(f"The second and the second to last characters are different")

