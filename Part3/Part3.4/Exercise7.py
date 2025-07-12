def squared(word, number):

    count = 0
    sentence = word * 1000000
    result = 0

    while True:
        count += 1
        if count <= number:
            print(sentence[result:result+number])
            result = result + number
        else:
            break


# You can test your function by calling it within the following block
if __name__ == "__main__":
    squared("abc", 5)
