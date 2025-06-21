word = input("Word: ")
space_left = " " * int(((((30 - len(word)) / 2) - 1)))
space_right = " " * int(((((30 - len(word)) / 2) - 1)))
result = "*" + space_left + word + space_right + "*"

print("*" * 30)

if len(result) % 2 != 0:
    space_left = " " * int(((((30 - len(word)) / 2))))
    result = "*" + space_left + word + space_right + "*"
    print(result)
else:
    print(result)
print("*" * 30)