def print_table(matrix):
    for row in matrix:
        for j in row:
            print(j, end='  ')
        print()


# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_table(matrix)



# 1  2  3  
# 4  5  6  
# 7  8  9  