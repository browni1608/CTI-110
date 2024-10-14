 # In class example of branching \
# GEt age from user

user_age=int(input("Give age : "))

# if else satement to determine age group 
if user_age >= 65:
    age_group = "senior citizen"
elif user_age < 5:
    age_group = "Toddler"
elif user_age > 12 and user_age < 20 :
    age_group = "Teenager"
else:
    age_group="not a senior"

# display result to user
print(f"You are {user_age} and your age group is : {age_group}")
