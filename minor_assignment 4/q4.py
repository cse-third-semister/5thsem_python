# Input: Original list and the element to remove
my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_remove = int(input("Enter the element to remove: "))

# Remove all occurrences of the element
my_list = [item for item in my_list if item != element_to_remove]

# Output the updated list
print("Updated list:", my_list)



# Enter the element to remove: 4
# Updated list: [1, 2, 3, 2, 2, 5]