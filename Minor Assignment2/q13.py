position = input("enter possition")

column = position[0]
row = int(position[1])

if (ord(column) - ord('a')) % 2 == row % 2:
    print("Black")
else:
    print("White")
