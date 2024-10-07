# Isaiah
 # 9/23/2024
 # P1HW2

 # Calculate users budget after traveling
print("This progam calculates and displays travel expenses")
budget=float(input(f"Enter your initial budget: "))
destination=input("Enter your travel destination:  ")
GasBudget=float(input(f"How much will you spend on Gas?"))
FoodBudget=float(input(f"How much do you need for food?"))
AccomodationBudget=float(input(f"Approximately, how much will you need for accomodaion/hotel?"))

print("-------Travel Expenses--------")

print(f"Location:{destination}")
print(f"Inintial Budget:${budget:.2f}")

print()

print(f"Fuel:${GasBudget:.2f}")
print(f"Accomodation:${AccomodationBudget:.2f}")
print(f"Food:${FoodBudget:.2f}")
print()

itemtotal=GasBudget+AccomodationBudget+FoodBudget
print("--------Travel Expenes-----------")
print(f"{'Location:':<25}{destination:<25}")
print(f"{'Initial Budget:':<25}${budget:<25.2f}")
print(f"{'Fuel:':<25}${GasBudget:<25.2f}")
print(f"{'Accomodation:':<25}${AccomodationBudget:<25.2f}")
print(f"{'Food:':<25}${FoodBudget:<25.2f}")
print("--------------------------------------")

print(f"{'Remaining Balance:':<25}${budget-itemtotal:.2f}")
