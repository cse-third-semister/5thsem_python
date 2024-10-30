def func():
    sum = 0
    for i in range(1, 51):
        if i % 2 == 0:
            sum = sum + (i ** 2)
    return sum

print(func())


# 22100