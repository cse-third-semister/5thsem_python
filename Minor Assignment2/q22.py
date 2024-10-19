n = int(input("Enter a number"))


while(n>=10):
    sum = 0
    while(n!=0):
        rem = n % 10
        sum = sum + rem
        n = n // 10
    n = sum
print("Value is ", n)

    