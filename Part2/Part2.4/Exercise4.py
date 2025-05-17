password = input("Password: ")

while True:
    passwordrepeat = input("Repeat password: ")
    if password == passwordrepeat:
        break
    print("They do not match!")

print("User account created!")