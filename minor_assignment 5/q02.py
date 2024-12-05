
n = int(input("How many student you want:\t"))
dict = {}
for i in range(n):
    name = input("Enter student name:\t")
    mark = int(input(f'Enter percentage of {name}:\t'))
    dict[name] = mark
    

print(dict)


# How many student you want:      1
# Enter student name:     rama
# Enter percentage of rama:       80
# {'rama': 80}