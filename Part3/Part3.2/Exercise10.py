word = input("Please type in a string: ")
count = 0

while count <= len(word):
    print(word[:count])
    count += 1