

import math

numbers = list(map(float, input("Enter 10 numbers: ").split()))
mean = sum(numbers) / len(numbers)
std_dev = math.sqrt(sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1))

print("Mean:", mean)
print("Standard Deviation:", std_dev)