string = input("Enter a string: ")

for i in range(len(string)):
    s = ""
    for j in range(i , len(string)):
        s += string[j]
       
        print(s)
