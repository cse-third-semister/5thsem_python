def is_armstrong(number):
    original_number = number
    num_digits = 0
    sum_of_powers = 0
    
    
    temp = number
    while temp > 0:
        temp //= 10
        num_digits += 1
    
    
    temp = number
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10
    
    return sum_of_powers == original_number 


print(is_armstrong(153))   
print(is_armstrong(1634))  
print(is_armstrong(123))   
