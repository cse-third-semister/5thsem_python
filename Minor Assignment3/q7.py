def func(c):
    if c in ['a', 'e', 'i', 'o', 'u']:
        print("It is a vowel")
    else:
        print("It is not a vowel")

c = input("Enter a character").lower()
func(c)
