str = "mississippi"
dic = {}
for s in str:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
print(dic)

# {'m': 1, 'i': 4, 's': 4, 'p': 2}