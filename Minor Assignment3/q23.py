def vowel_indices(string):
    vowels = "aeiouAEIOU"
    indices = []
    for i in range(len(string)):
        if string[i] in vowels:
            indices.append(i)
    return indices

s = input("Enter a word")
print(vowel_indices(s))
