def are_coprime():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    if gcd(a, b) == 1:
        print(f"{a} and {b} are coprime.")
    else:
        print(f"{a} and {b} are not coprime.")

are_coprime()
