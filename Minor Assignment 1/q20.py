"""
Create a program that reads two integers, a and b, from the user. Your program should compute and
 display:
 2

 • The sum of a and b
 • The difference when b is subtracted from a
 • The product of a and b
 • The quotient when a is divided by b
 • The remainder when a is divided by b
 • The result of log10 a
 • The result of ab
 Hint: You will probably find the log10 function in the math module helpful for computing the
 second last item in the list
"""
import math

a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))

sum_result = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b
log_a = math.log10(a)
power = a ** b

print("Sum of a and b:", sum_result)
print("Difference when b is subtracted from a:", difference)
print("Product of a and b:", product)
print("Quotient when a is divided by b:", quotient)
print("Remainder when a is divided by b:", remainder)
print("log10 of a:", log_a)
print("Result of a^b:", power)


# Enter the first integer (a): 2
# Enter the second integer (b): 3
# Sum of a and b: 5
# Difference when b is subtracted from a: -1
# Product of a and b: 6
# Quotient when a is divided by b: 0.6666666666666666
# Remainder when a is divided by b: 2
# log10 of a: 0.3010299956639812
# Result of a^b: 8
