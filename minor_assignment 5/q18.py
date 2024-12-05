def analyze_sets(list1, list2):
    set1, set2 = set(list1), set(list2)
    sym_diff = set1 ^ set2
    print(sym_diff)
    modified = [(x * 2 if x % 2 == 0 else x + 5) for x in sym_diff]
    return sorted(modified)

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(analyze_sets(list1, list2))  # Output: [7, 7, 10, 12]




# [4, 6, 10, 12]