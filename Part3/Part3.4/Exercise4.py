# Write your solution here
def print_many_times(name, times):
    index = 0 
    while times > index:
        print(name)
        index += 1
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)