n = int(input("Enter a number"))
list = []
while(n!=1):
    for i in range(2,n+1):
        if(n%i==0):
            list.append(i)
            n = n // i
            break

print(list)  