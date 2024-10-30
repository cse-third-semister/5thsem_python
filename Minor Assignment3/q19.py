def gcd(a, b):
    while b != 0:
        
        remainder = a % b
        a = b  
        b = remainder 
    
    return a


num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is", result)  
