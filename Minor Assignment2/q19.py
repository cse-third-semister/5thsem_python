n  = int(input("Enter a number"))
rev = 0
i  = n
while(i!=0):
    rem = i % 10
    rev = (rev * 10 )+ rem
    i = i//10
  
print("Reverse number is ", rev)