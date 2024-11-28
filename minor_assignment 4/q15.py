import random

# Generate a 4x4 matrix with random 0s and 1s
l = []
for i in range(4):
    l.append([random.randrange(0, 2) for j in range(4)])

# Print the matrix
for row in l:
    print("".join(map(str, row)))

# Find the row with the most 1s
row = -1
max_sum = -1

for i in range(len(l)):
    if sum(l[i]) > max_sum:
        row = i
        max_sum = sum(l[i])

# Find the column with the most 1s
col = -1
max_col_sum = -1

for j in range(4):
    col_sum = sum(l[i][j] for i in range(4))
    if col_sum > max_col_sum:
        col = j
        max_col_sum = col_sum

# Output the results
print(f"The largest row index: {row}")
print(f"The largest column index: {col}")
