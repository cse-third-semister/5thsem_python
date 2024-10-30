n = int(input("Enter a number"))
l = len(str(n))
list = []
def func(n):
    while(n != 0):
        rem = n % 10
        list.append(rem)
        n = n // 10
func(n)
list.sort() 
print(list[l-1])
print(list[l-2])
print(list[l-3])
