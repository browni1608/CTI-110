#Isaiah Brown
# 10/14/2024
#P3HW1
# Use branchin to determine letter grade
Module1 = float(input("Enter Grade for Module 1:"))
Module2 = float(input("Enter Grade for Module 2:"))
Module3 = float(input("Enter Grade for Module 3:"))
Module4 = float(input("Enter Grade for Module 4:"))
Module5 = float(input("Enter Grade for Module 5:"))
Module6 = float(input("Enter Grade for Module 6:"))
module=[Module1,Module2,Module3,Module4,Module5,Module6]
print()
print("-------------Results-------------")

print(f"{'Lowest grade:':<15}{min(module)}")
print(f"{'Highest grade:':<15}{max(module)}")
print(f"{'Sum of grades:':<15}{sum(module)}")
print(f"{'Lowest grade:':<15}{min(module)}")
print(f"{'Average:':<15} {sum(module) / len(module):.2f}")
Average=sum(module) / len(module)
# Create branching to get leter grade
if Average>=90:
    letter_grade = "A"
elif Average>=80:
    letter_grade = "B"
elif Average>=70:
    letter_grade = "C"
elif Average>=60:
    letter_grade = "D"
else:
    letter_grade = "F"

    #display results
print(f"The average is {Average:.2f} -- Letter Grade: {letter_grade}")
print("----------------------------------")
