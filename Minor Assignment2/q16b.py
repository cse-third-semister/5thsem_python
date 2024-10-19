import math

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
sum_series = 1

for i in range(1, n + 1):
    term = (x ** i) / math.factorial(i)
    sum_series += term

print("Sum of the series:", sum_series)
