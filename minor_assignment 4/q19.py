import copy

def demonstrate_copy():
 
    original_list = [['Shallow', 2, 3], [4, 5, 6]]
    print("Original List:", original_list)

   
    shallow_copy = copy.copy(original_list)
   
    deep_copy = copy.deepcopy(original_list)

  
    shallow_copy[0][0] = 'Modified'
    print("\nAfter modifying shallow copy:")
    print("Original List:", original_list)
    print("Shallow Copy:", shallow_copy)

   
    deep_copy[1][0] = 'Deep'
    print("\nAfter modifying deep copy:")
    print("Original List:", original_list)
    print("Deep Copy:", deep_copy)


demonstrate_copy()


# Original List: [['Shallow', 2, 3], [4, 5, 6]]

# After modifying shallow copy:
# Original List: [['Modified', 2, 3], [4, 5, 6]]
# Shallow Copy: [['Modified', 2, 3], [4, 5, 6]] 

# After modifying deep copy:
# Original List: [['Modified', 2, 3], [4, 5, 6]]
# Deep Copy: [['Shallow', 2, 3], ['Deep', 5, 6]]