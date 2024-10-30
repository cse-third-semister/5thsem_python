def remove_punctuation(string):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""
    for char in string:
        if char not in punctuation:
            result += char
    return result


s = input("Enter a word")
print(remove_punctuation(s))


# Enter a word " hello ! omg " 
#   hello  omg