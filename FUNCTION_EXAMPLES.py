# Learning to use user-defined functions

# Define a add function 
def add(num1, num2, num3):
    product = num1 + num2 + num3
    print(product)

# Define a multiply function 
def multiply(num1, num2, num3):
    product = num1 * num2 * num3
    print(product)
def returnNum():
    userInput = input("Give me a big number: ")
    while not userInput.isn99umeric():
        print("value mut be a number")
def getName(lastName):
    name = input("Enter your first name")
    fullname = "*******"+ name + "**********" + lastName
    return fullname
# DEfine main function - all your logic goes here
def main():
    first_num = int(input("Gimmie a  numer"))
    second_num = int(input("Gimmie a number"))
    third_num = int(input("Gimmie a number"))
    # Call the multiply fnction 
    multiply(first_num,second_num,third_num)

    # Call the add function 
    add(first_num, second_num, third_num)
# Call value returning fnc
bigNum = returnNum()

print(bigNum * 5)

print(getName("Brown"))
# Call main function 
if __name__ == "_main_":
    main()
e