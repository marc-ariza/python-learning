word = input("Please type in a word: ")
letter = input("Please type in a character: ")
position = word.find(letter) 
all_positions = position + 3

lenght = len(word)
if all_positions <= lenght:
    print(word[position:all_positions])
else:
    print("")

