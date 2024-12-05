set1 = {10, 20, 30}
set2 = {5, 10, 15, 20}

a = set1 - set2                
b = set1 ^ set2  
c = set1 | set2                
d = set1 & set2                

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)





# a: {30}
# b: {5, 30, 15}
# c: {20, 5, 10, 30, 15}
# d: {10, 20}