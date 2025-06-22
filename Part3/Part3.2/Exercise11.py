word = input("Please type in a string: ")
count = 1
length = len(word) - 1

while length >= 0:
    print(word[length:])
    length -= 1