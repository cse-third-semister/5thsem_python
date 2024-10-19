
c = input("Enter s to start")
while(c!=0):
   
    print("""
    enter 1 for + 
    enter 2 for -
    enter 3 for *
    enter 4 for /
    enter 0 for exit
      
    """)

    c = input("Enter your choice: ")

    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    if(c=="1"):
        print(f"a + b = {a+b}")
    elif(c=="2"):
        print(f"a - b = {a-b}")
    elif(c=="3"):
        print(f"a * b = {a*b}")
    elif(c=="4"):
        if(b==0):
            print("Error! Division by zero is not allowed")
            continue
        else:

            print(f"a / b = {a/b}")
    elif(c=="0"):
        break
    else:
        print("Invalid choice")
    








