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
