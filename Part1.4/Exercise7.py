timescafe = int(input("How many times a week do you eat at the student cafeteria? "))
pricecafe = float(input("The price of a typical student lunch? "))
pricegroceries = float(input("How much money do you spend on groceries in a week? "))

pricedaily = (pricegroceries + timescafe * pricecafe) / 7
priceweekly = pricedaily * 7

print("Average food expenditure:")
print(f"Daily: {pricedaily} euros")
print(f"Weekly: {priceweekly} euros")



