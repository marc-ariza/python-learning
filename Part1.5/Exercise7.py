hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day = input("Day of the week: ")

if day == "Sunday":
    hourly_wage *= 2

daily_wage = hourly_wage * hours_worked

print(f"Daily wages: {daily_wage} euros")