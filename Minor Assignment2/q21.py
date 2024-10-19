n = int(input("Enter a number  "))
fact = 1
b = False
if(n==0):
    print("yes it is a factorial")
else:
    for i in range(1,n+1):
        fact  = fact * i
        if(fact==n):
            b = True
        if(fact>=n):
            break

    if(b):
        print("Yes ,It is factorial number")
    else :
        print("No it is not")

