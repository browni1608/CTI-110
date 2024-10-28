# while loops examples
# Program only runs if user says yes
userChoice = input("Wanna run program? ") .lower()

while userChoice == "yes" :
    print("***:" * 10)
    print("Programming is running")
    print()
    userChoice = input("Run again? ").lower()
# Loop ends/breaks
print("Thanks for using the program")

# numeric variable to control loop
controller = 0
max_value = int(input("Enter max value: "))
while controller <= max_value:
    #Add one to controller
    print(controller)
    controller += 1
    
#Loop breaks
print(f"loop broke bc controller hit max volume")
print("controller is " , controller)
