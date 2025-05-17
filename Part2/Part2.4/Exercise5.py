attempts = 0
correctpin = 4321

while True:
    attemptedpin = int(input("PIN: "))
    attempts += 1

    if attemptedpin != correctpin:
        print("Wrong")
    else:
        break


if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")



