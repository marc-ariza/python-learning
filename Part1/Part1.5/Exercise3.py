name = input("Please tell me your name: ")

if name != "Jerry":
    portionstotalprice = int(input("How many portions of soup? "))
    portion_price = 5.9
    portionstotalprice *= portion_price
    print(f"The total cost is {portionstotalprice}")


print("Next please!")
