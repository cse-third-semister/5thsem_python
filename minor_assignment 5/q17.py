set1 = {'red', 'green', 'blue'}
set2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

# Part a: Comparison operators
print("set1 == set2:", set1 == set2)
print("set1 != set2:", set1 != set2)
print("set1 < set2:", set1 < set2)   # Proper subset
print("set1 <= set2:", set1 <= set2) # Subset
print("set1 > set2:", set1 > set2)   # Proper superset
print("set1 >= set2:", set1 >= set2) # Superset

# Part b: Mathematical set operators
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Difference (set2 - set1):", set2 - set1)
print("Symmetric Difference:", set1 ^ set2)




# set1 == set2: False
# set1 != set2: True
# set1 < set2: True
# set1 <= set2: True
# set1 > set2: False
# set1 >= set2: False
# Union: {'blue', 'cyan', 'red', 'magenta', 'green'}
# Intersection: {'blue', 'red', 'green'}
# Difference (set1 - set2): set()
# Difference (set2 - set1): {'magenta', 'cyan'}
# Symmetric Difference: {'cyan', 'magenta'}