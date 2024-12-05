n = int(input("How many student you want:\t"))
dict = {}
for i in range(n):
    name = input("Enter student name:\t")
    mark = int(input(f'Enter marks of {name}:\t'))
    dict[name] = mark
    
print("You can see your mark by entering your name:\t")
name = input("Enter student name:\t")
print(f'The mark of student is {dict[name]}:\t')




# How many student you want:      2
# Enter student name:     jyoti
# Enter marks of jyoti:   10
# Enter student name:     hari
# Enter marks of hari:    20
# You can see your mark by entering your name:
# Enter student name:     jyoti
# The mark of student is 10: