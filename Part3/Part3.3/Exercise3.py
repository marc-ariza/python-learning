
while True:

    number = int(input("Please type in a number: "))
    end = number
    result = 1

    if number <= 0:
        break
    
    while end >= 1:
        result = result * end
        end -= 1
    print(f"The factorial of the number {number} is {result}")

print("Thanks and bye!")