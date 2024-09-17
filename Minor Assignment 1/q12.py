"""

12. Write a program that begins by reading a radius, r, from the user. The program will continue by
 computing and displaying the area of a circle with radius r and the volume of a sphere with radius r.
 Use the pi constant in the math module in your calculations.
 Hint: The area of a circle is computed using the formula area = πr2.
 The volume of a sphere is computed using the formula volume = 4
 3
 πr3
"""

import math
r = int(input("Enter radius : "))
print("Area of the circle is",math.pi*pow(r,2))
print("volume of the circle is",4/3*math.pi*pow(r,3))

# Enter radius : 3
# Area of the circle is 28.274333882308138
# volume of the cir733552923254cle is 113.09