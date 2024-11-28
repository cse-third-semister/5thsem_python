def sum_numbers(tuples):
    total = 0
    for t in tuples:
        for num in t:
            if type(num) in (int, float):
                total += num
    print(total)

# Example usage
sum_numbers(((1, 2), (3.5, 4), (5, 6)))
