width = int(input("Width: "))
height = int(input("Height: "))
result = ""
 
while height > 0:
    result = result + ("#"*width)
    result = (f"{result}\n")
    height -= 1
print(result)