def are_coprime():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    def gcd(x, y):
        while y!=0:
            rem = x %y 
            x = y
            y = rem
            # x, y = y, x % y
        return x
    
    if gcd(a, b) == 1:
        print(f"{a} and {b} are coprime.")
    else:
        print(f"{a} and {b} are not coprime.")

are_coprime()


# Enter the first number: 10
# Enter the second number: 20
# 10 and 20 are not coprime.