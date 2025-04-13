nota = int(input("How many points [0-100]: "))

if nota < 0:
    print("Grade: impossible!")
elif nota >= 0 and nota <= 49:
    print("Grade: fail")
elif nota >= 50 and nota <= 59:
    print("Grade: 1")
elif nota >= 60 and nota <= 69:
    print("Grade: 2")
elif nota >= 70 and nota <= 79:
    print("Grade: 3")
elif nota >= 80 and nota <= 89:
    print("Grade: 4")
elif nota >= 90 and nota <= 100:
    print("Grade: 5")
else:
    print("impossible!")