input1 = input("Please type in a string 1: ")
input2 = input("Please type in a string 2: ")

if len(input1) > len(input2):
    print(f"{input1} is longer")
elif len(input2) > len(input1):
    print(f"{input2} is longer")
else:
    print("The strings are equally long")