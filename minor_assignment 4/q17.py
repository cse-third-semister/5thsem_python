import math

numbers = list(map(float, input("Enter ten numbers: ").split()))
if len(numbers) == 10:
    mean = sum(numbers) / 10
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in numbers) / 9)
    print(f"The mean is {mean:.2f}\nThe standard deviation is {std_dev:.5f}")
else:
    print("Error: Enter exactly 10 numbers.")



# Enter ten numbers: 1.9 2.5 3.7 2 1 6 3 4 5 2
# The mean is 3.11
# The standard deviation is 1.55738