def arithmetic_progression():
    first_term = int(input("Enter the first term: "))
    common_difference = int(input("Enter the common difference: "))
    for i in range(10):
        term = first_term + i * common_difference
        print(term)

arithmetic_progression()
