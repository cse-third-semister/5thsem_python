def shift_letters():
    string = input("Enter a string of lowercase alphabets: ")
    shifted_string = ""
    
    for char in string:
        if char == 'z':
            shifted_string += 'a'
        else:
            shifted_string += chr(ord(char) + 1)
    
    print(shifted_string)

shift_letters()
