n = int(input("Enter a number : "))
b = False
sum = 0
for i in range(2,n+1):
    for j in range(2,i):
        if (i % j == 0):
            b = True
            break
    if(b==False):
        sum = sum + i
    else :
        b = False

        
       
print(f"The sum of prime number below {n} is {sum}")

