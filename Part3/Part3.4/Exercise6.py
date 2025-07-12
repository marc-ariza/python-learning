# Write your solution here
def chessboard(number):
    width = 0
    result = ""
    loop = 0

    while loop < number:
        while True:
            if width < number:
                result += "1"
                width += 1
            else:
                result = (f"{result}\n")
                width = 0
                loop += 1 
                break
            if width < number:
                result += "0"
                width += 1
            else:
                result = (f"{result}\n")
                width = 0
                loop += 1 
                break

        if loop >= number:
            break

        while True:
            if width < number:
                result += "0"
                width += 1
            else:
                result = (f"{result}\n")
                width = 0
                loop += 1 
                break
            if width < number:
                result += "1"
                width += 1
            else:
                result = (f"{result}\n") 
                width = 0
                loop += 1
                break
        
    print(result)

# Testing the function
if __name__ == "__main__":
    chessboard(4)
