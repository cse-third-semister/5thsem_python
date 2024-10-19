n = int(input("Enter a number : "))
b = False
for i in range(2,n):
    if n % i == 0:
        b =True
        break
if(b):
    print("It is not a prime")
else :
    print("It is prime")

