year = int(input("Year: "))
leapyear = year + 1

while True: 
    if leapyear % 4 == 0 and leapyear % 100 == 0 and leapyear % 400 != 0:
        leapyear += 1
    elif leapyear % 4 == 0:
        break
    else:
        leapyear += 1

print(f"The next leap year after {year} is {leapyear}")