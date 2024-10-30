def number_to_text():
    num_to_text = [
        'zero', 'one', 'two', 'three', 'four', 
        'five', 'six', 'seven', 'eight', 'nine'
    ]

    number = int(input("Enter a positive number: "))
    s = ""
    i = number
    
    while i > 0:
        rem = i % 10
        s = num_to_text[rem] + " " + s
        i //= 10
          
    
    
    print(s) 
number_to_text()


# Enter a positive number: 10
# one zero 