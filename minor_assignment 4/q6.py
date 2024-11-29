# Input 10 integers from the keyboard into a list. The number to be searched is entered through the
# keyboard by the user. Write a Python program to find if the number to be searched is present in the
# list and if it is present, display the number of times it appears in the list.

lst = [int(input("Enter element: ")) for _ in range(10)]
search = int(input("Enter number to search: "))
count = lst.count(search)
print(f"Number {search} appears {count} times." if count > 0 else "Number not found.")




# Enter element: 2
# Enter element: 3
# Enter element: 4
# Enter element: 5
# Enter element: 6
# Enter element: 7
# Enter element: 8
# Enter element: 9
# Enter element: 10
# Enter number to search: 7
# Number 7 appears 1 times.