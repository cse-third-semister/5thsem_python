def unique_pairs(words):
    words = [word for word in words if len(word) >= 4]
    result = set()
    
    for i in words:
        for j in range(len(words)):
            if i != words[j] and not set(i) & set(words[j]):
                result.add(tuple(sorted((i, words[j]))))
    
    return result

# Example usage:
words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]
print(unique_pairs(words))




# {('dogs', 'zebra'), ('apple', 'fish'), ('fish', 'zebra'), ('lion', 'zebra'), ('apple', 'bird'), ('apple', 'dogs')}