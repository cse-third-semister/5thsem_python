list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
n = input("Enter a number")
s = ""
l = 10 ** (len(str(n)) -1)

n = int(n)
while(n!=0):
        rem = n // l
        print("rem",rem)
        s = s + list[rem]+" "
        n = n - (l*rem)
        l = l //10


   
print(s)
