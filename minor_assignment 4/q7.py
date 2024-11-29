n = int(input("Enter how many number you want to add:\t"))
lis = []

for i in range(n):
    num = int(input("Enter a number: "))
    lis.append(num)

for i in range(1,n):
    
    sum = lis[i] + lis[i-1]
    lis.pop(i)
    lis.insert(i,sum )

print(lis)

# Enter how many number you want to add:  2
# Enter a number: 40
# Enter a number: 50
# [40, 90]