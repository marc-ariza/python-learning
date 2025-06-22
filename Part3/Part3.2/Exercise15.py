string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

current_position = 0
substring_number = 1

while current_position < len(string):
    current_position =+ 1

    if string.find(substring) == -1:
        print("The substring does not occur twice in the string.")
        break
    
    index1 = string.find(substring) + len(substring)
    index2 = string.find(substring, index1)

    if index2 == -1:
        print("The substring does not occur twice in the string.")
        break
    else:
        print(f"The second occurrence of the substring is at index {index2}.")
        break





