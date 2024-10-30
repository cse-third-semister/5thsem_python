def product_of_digits():
    number = input("Enter a number: ")
    product = 1
    
    for digit in number:
        product *= int(digit)
    
    print("Product of digits:", product)

product_of_digits()

# Enter a number: 30
# Product of digits: 0
