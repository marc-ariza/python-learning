word = input("Please type in a word: ")
character = input("Please type in a character: ")

current_position = 0
while current_position < len(word):
    index = word.find(character, current_position)

    if index == -1:
        break
    if index + 2 < len(word) :
        print(word[index:index + 3])

    current_position = index + 1