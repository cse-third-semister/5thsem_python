import random

# Input: Size of the list
N = int(input("Enter the size of the list: "))

# Create a list with random values
random_list = list(random.randint(1, 100) for i in range(N))

# Calculate sum and average
total_sum = sum(random_list)
average = total_sum / N if N > 0 else 0

# Output results
print(f"List: {random_list}")
print(f"Sum: {total_sum}, Average: {average:.2f}")
