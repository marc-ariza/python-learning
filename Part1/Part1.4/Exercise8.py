numstudents = int(input("How many students on the course? "))
numsize = int(input("Desired group size? "))
numgroups = numstudents // numsize
nummodulo = numstudents % numsize

if nummodulo == 0:
    print(f"Number of groups formed: {numgroups}")
else:
    numgroups += 1
    print(f"Number of groups formed: {numgroups}")
    

