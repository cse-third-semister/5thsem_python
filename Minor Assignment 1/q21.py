"""

 21. Write a program that determines how quickly an object is travelling when it hits the ground. The user
 will enter the height from which the object is dropped in meters (m). Because the object is dropped
 its initial speed is 0 m/s. Assume that the acceleration due to gravity is 9.8m/s2. You can use the
 formula vf= (v2
 i +2ad) to compute the final speed, vf, when the initial speed, vi, acceleration, a,
 and distance, d, are known
"""
import math

height = float(input("Enter the height from which the object is dropped (in meters): "))
g = 9.8
v_i = 0 

final_speed = math.sqrt(v_i**2 + 2 * g * height)
    

print(f"The final speed of the object when it hits the ground is {final_speed:.2f} m/s")



# Enter the height from which the object is dropped (in meters): 5
# The final speed of the object when it hits the ground is 9.90 m/s