def replace_vowels():
    string = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char in vowels:
            result += "*"
        else:
            result += char
    print(result)

replace_vowels()


# Enter a string: hello
# h*ll*