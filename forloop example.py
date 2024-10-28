
# For loop with range - one parameter

for item in range(5):
    print(item)
print()
 # For loop with range - 2 parameters   
for branch in range(3,10):
    print(branch)
#for loop with range 3 parameters
# ramge(start,stop,step) - stop is not included 
print("Pairs of cats")
for cat in range(2,21,2):
    print(cat)
 # print all values in list
trees = ["Pine", "Dogwood", "Palm","Oak"]
print("Lemme tell ya about trees")
for tree in trees:
    print(tree, "tree")
    print("***********")

num_list = [0,-7,2,8]
num_sum = 0 
for num in num_list:
    num_sum += num
# Loop breaks
print("Final sum is", num_sum)
