# formatting output using F string
# variables like hw2
name = "Macy"
address = "123 Union st"
age = 3
cost = 2500
isCute = True
cost_to_feed = 2500.99


print("*-" * 20)
print(f"{'Name:':<18}{name:<25}")
print(f"{'Address:':<18}{address:<25}")
print(f"{'Age:':<18}{age:<25}")
print(f"{'Cost to buy:':<18}${cost:<25,.2f}")
print(f"{'Cost to feed:':<18}${cost_to_feed:<25,.2f}")
print(f"{'Is Macy cute?':<18}{str(isCute):<25}")
