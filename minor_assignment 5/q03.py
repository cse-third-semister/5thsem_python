n = int(input("How many student you want:\t"))
dict = {}
for i in range(n):
    value = int(input("Enter sl no:\t"))
    mark = int(input(f'Enter value:\t'))
    dict[value] = mark
    

sum = 0
for value in dict.values():
    sum = sum + value
print(sum)


# How many student you want:      1
# Enter sl no:    1
# Enter value:    12
# 12