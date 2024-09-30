# Isaiah Brown
 # 9/30/202
 # P2LAB1
 # Using imported library, math, and f strng

import math

 # Get radius from user
radius = float(input("What is the radius of the circle?"))
print()

# Calculate diameter
diameter = 2 * radius

# display diameter with 1 decimal place 
print(f"The diameter of the circle is {diameter:.1f}\n")

# Calculate circumference
circum = 2 * math.pi * radius

# display circumference with 2 decimal place
print(f"The cicrcumference of the circle is {circum:.2f}\n")

# Calculate the area
area = math.pi * (radius ** 2)
area2 = math.pi * math.pow(radius, 2)
#Display area
print(f"The area of the circle is {area:.3f} \n")
