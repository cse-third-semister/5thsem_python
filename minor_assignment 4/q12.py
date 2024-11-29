


matrix = []

# Input the matrix using two for loops
print("Enter a 3-by-4 matrix row by row:")
for i in range(3):  # Loop for rows
    row = []
    for j in range(4):  # Loop for columns
        value = float(input(f" row {i + 1}, column {j + 1}: "))
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



# Enter a 3-by-4 matrix row by row:
#  row 1, column 1: 1
#  row 1, column 2: 0
#  row 1, column 3: 1
#  row 1, column 4: 0
#  row 2, column 1: 1
#  row 2, column 3: 1
#  row 2, column 4: 2
#  row 3, column 1: 1
#  row 3, column 2: 2
#  row 3, column 3: 1
#  row 3, column 4: 0
# Sum of column 0 : 3.0
# Sum of column 1 : 4.0
# Sum of column 2 : 3.0
# Sum of column 3 : 2.0