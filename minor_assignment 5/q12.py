s = input("Enter a sentence: ").lower().split()
word_count = {word: s.count(word) for word in set(s)}
print(word_count)
duplicates = {w:c for w,c in word_count.items() if c>1}

print("Number of duplicate words:", len(duplicates))
print("Duplicates:", duplicates)



# Enter a sentence: i am a boy she is a girl
# {'i': 1, 'am': 1, 'a': 2, 'boy': 1, 'is': 1, 'girl': 1, 'she': 1}
# Number of duplicate words: 1
# Duplicates: {'a': 2}