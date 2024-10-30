freq = {}
def count(word):
   
    for c in word:
        freq[c] = word.count(c)
    
    return check()

def check():
    odd = 0
   
    for value in freq.values():
        if(value % 2 !=0):
            odd += 1
    if(odd == 1):
        return True
    else:
        return False
      


word  = input("Enter a word :  ")
if(count(word)):
    print("This can be rearranged to form a palindrome.")
else:
    print("This can not be rearranged to form a palindrome.")


