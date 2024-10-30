def is_perfect_number():
    number = int(input("Enter a positive integer: "))
    divisors_sum = 0
    
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    
    if divisors_sum == number:
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")

is_perfect_number()
