def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    result = ''
    
    for char in text:
        if char not in vowels:
            result += char  
    
    return result


s = input("Enter a string")
result = remove_vowels(s)
print(result) 


# Enter a string hello
#  hll