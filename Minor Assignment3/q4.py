def func(s, l):
    st = ""
    for i in range(l-1, -1, -1):
        st = st + s[i]
    return st

s = input("Enter a string")
l = len(s)
print(func(s, l))


# Enter a string hello 
# olleh