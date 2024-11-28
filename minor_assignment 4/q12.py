


matrix = []

# Input the matrix using two for loops
print("Enter a 3-by-4 matrix row by row:")
for i in range(3):  # Loop for rows
    row = []
    for j in range(4):  # Loop for columns
        value = float(input(f"Enter value for row {i + 1}, column {j + 1}: "))
        row.append(value)
    matrix.append(row)



def column_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sums = []
    for col in range(cols):
        total = 0
        for row in range(rows):
            total += matrix[row][col]
        sums.append(total)
    return sums



# Compute and display the column sums
col_sums = column_sum(matrix)
for i in range(len(col_sums)):
    print("Sum of column", i, ":", col_sums[i])

