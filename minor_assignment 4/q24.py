# Input: List of tuples and the desired length to remove
list_of_tuples = [(1, 2), (3,), (4, 5, 6), (7, 8), (), (9, 10, 11, 12)]
K = int(input("Enter the length of tuples to remove: "))

# Removing tuples with length K
filtered_list = list(filter(lambda x: len(x)!=K ,list_of_tuples))

# Output: Filtered list
print("Filtered list:", filtered_list)



# Enter the length of tuples to remove: 2
# Filtered list: [(3,), (4, 5, 6), (), (9, 10, 11, 12)]