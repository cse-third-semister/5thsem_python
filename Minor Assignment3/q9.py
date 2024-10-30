def binarytodecimal(n):
    s = str(n)
    l = len(str(n))
    j = k = n
    i = 0
    pow = 2
    sum1 = 0
    for i in range(l-1,-1,-1):
        sum1 = sum1 + ( (pow ** i) * (int(s[i])))
        i = i+1
        
    return sum1


def decimatobinary(n):
    s = ""
    
    k = n
    i = 0
    pow = 2
    sum1 = 0
    while(k!=0):
        s = str(k % 2) + s
        k = k // 2
    return s
print(binarytodecimal(10101))
print(decimatobinary(20))