str = "mississippi"
dic = {}
for s in str:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

for key,value in dic.items():
    if(key  in "aeiou"):
        print(f'{key}:{value}')



# i:4