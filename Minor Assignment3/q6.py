def func(s, l):
    st = ""
    for i in range(l-1, -1, -1):
        st = st + s[i]
    return st

s = input("Enter a string")
l = len(s)
stt = func(s, l)
if stt == s:
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")


# Enter a string India
# No, it is not a palindrome