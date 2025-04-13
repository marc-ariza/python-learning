# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))


x = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x_negative = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print(f"The roots are {x} and {x_negative}")

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5