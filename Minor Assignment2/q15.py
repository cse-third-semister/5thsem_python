num = int(input("Enter a natural number: "))
sum_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
