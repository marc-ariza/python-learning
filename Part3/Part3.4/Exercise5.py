# Write your solution here
def hash_square(number):
    result = ""
    height = 0

    while height < number:
        result = result + (number * "#")
        result = (f"{result}\n")
        height += 1
    print(result)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)