number = int(input("Please type in a number: "))
start = 1

while start <= number:
    multiplier = 1
    while multiplier < number:
        print(f"{start} x {multiplier} = {start*multiplier}")
        multiplier += 1
    print(f"{start} x {multiplier} = {start*multiplier}")
    start += 1