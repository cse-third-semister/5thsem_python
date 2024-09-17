"""
 Write a program that reads three integers from the user and displays them in sorted order (from
 smallest to largest). Use the min and max functions to find the smallest and largest values. The middle
 value can be found by computing the sum of all three values, and then subtracting the minimum value
 and the maximum value.
"""
print("Enter 3 number")
num1 = int(input())
num2 = int(input())
num3 = int(input())

min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)

middle = (num1 + num2 + num3) - min_num - max_num


print(f"The numbers in sorted order are: {min_num}, {middle}, {max_num}")


# Enter 3 number
# 5
# 89
# -2
# The numbers in sorted order are: -2, 5, 89