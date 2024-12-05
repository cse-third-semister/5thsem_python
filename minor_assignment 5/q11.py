n = input("Enter number")
d = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', 
     '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
str = " "
for i in n:
    str += d[i] + " "


print(str)  


# Enter number157
#  One Five Seven