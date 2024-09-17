
n = int(input("Enter a four-digit number: "))


if 1000 <= n <= 9999:
    total_sum = 0
    while n != 0:
        total_sum += n % 10
        n = n // 10
    print(f"The sum of the digits is {total_sum}")
else:
    print("The number entered is not a four-digit integer.")
