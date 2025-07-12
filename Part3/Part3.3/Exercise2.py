sentence = input("Please type in a sentence: ")
space = " "
current_position = 0

print(sentence[0])

while True:

    index = sentence.find(space, current_position)
    if index == -1:
        break
    index += 1
    if index < len(sentence): 
        print(sentence[index])
    current_position = index  