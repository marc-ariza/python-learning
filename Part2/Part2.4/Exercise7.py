story = ""
lastword = ""

while True:
    word = input("Please type in a word: ")
    if word == "end" or word == lastword:
        break
    story += word + " "
    lastword = word

print(story)
