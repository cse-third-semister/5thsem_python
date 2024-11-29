my_list = []

while True:
    print("\nMenu:")
    print("1. Create a list ")
    print("2. Display the list ")
    print("3. Insert an element ")
    print("4. Delete an element ")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        N = int(input("Enter the size of the list: "))
        my_list = [int(input(f"Enter element {i+1}: ")) for i in range(N)]
    elif choice == 2:
        print("List elements:", my_list)
    elif choice == 3:
        elem = int(input("Enter the element: "))
        pos = int(input("Enter the position "))
      
        my_list.insert(pos, elem)
           
       
    elif choice == 4:
        pos = int(input("Enter the position "))
       

        my_list.pop(pos)
            
       
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice.")


# Menu:
# 1. Create a list     
# 2. Display the list  
# 3. Insert an element 
# 4. Delete an element 
# 5. Exit
# Enter your choice: 1 
# Enter the size of the list: 4
# Enter element 1: 1
# Enter element 2: 2
# Enter element 3: 3
# Enter element 4: 4

# Menu:
# 1. Create a list
# 2. Display the list
# 3. Insert an element
# 4. Delete an element
# 5. Exit
# Enter your choice: 2
# List elements: [1, 2, 3, 4]

# Menu:
# 1. Create a list
# 2. Display the list
# 3. Insert an element
# 4. Delete an element
# 5. Exit
# Enter your choice: 5
# Exiting the program.