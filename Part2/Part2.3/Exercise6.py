first_letter = input("1st letter: ")
second_letter = input("2nd letter: ")
third_letter = input("3rd letter: ")

if (first_letter > second_letter and second_letter > third_letter) or (second_letter > first_letter and third_letter > second_letter):
    middle_letter = second_letter
elif (first_letter > second_letter and third_letter > first_letter) or (second_letter > first_letter and first_letter > third_letter):
    middle_letter = first_letter
else:
    middle_letter = third_letter

print(f"The letter in the middle is {middle_letter}")