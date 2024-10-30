def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


n  = int(input("Enter nth number"))
print(f'The {n} number is {fibo(n-1)}')



# Enter nth number 6
# The 6 number is 5