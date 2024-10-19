import math

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
sum_series = 1

for i in range(1, n + 1):
    term = (-1) ** i * (x ** (2 * i)) / math.factorial(2 * i)
    sum_series += term

print("Sum of the series:", sum_series)
