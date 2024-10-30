def func(n):
    sum = 0
    while n != 0:
        sum = sum + 1
        n = n // 10
    return sum

n = int(input("Enter a number"))
print(func(n))


# Enter a number 20
# 2