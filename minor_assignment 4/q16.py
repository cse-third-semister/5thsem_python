l = [10, 1 ,1, 3 ,4, 4, 5, 7 ,9 ,11, 21]

l.pop(0)
print(l)
if(l == sorted(l)):
    print("sorted order")
else:
    print("not sorted order")