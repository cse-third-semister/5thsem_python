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