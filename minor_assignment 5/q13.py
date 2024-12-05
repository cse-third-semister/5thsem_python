def unique_words(words):
    
    unique = sorted(set(word.lower() for word in words))
    print("Unique words in alphabetical order:", unique)


sentence = input("Enter a sentence  :")
unique_words(sentence.split())


# Enter a sentence  :The world is very nice 
# Unique words in alphabetical order: ['is', 'nice', 'the', 'very', 'world']