n = int(input("Enter the number of terms: "))
sum_series = 0

for i in range(n):
    term = 2 * i + 1
    if i % 2 == 0:
        sum_series += term
    else:
        sum_series -= term

print("Sum of the series:", sum_series)
