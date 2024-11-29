# Define the rotate function
def rotate(arg1, arg2, arg3):
    return arg2, arg3, arg1

# Initialize variables
a, b, c = 'Doug', 22, 1984

# Call the function three times, unpacking the result
for i in range(3):
    a, b, c = rotate(a, b, c)
    print(f"a: {a}, b: {b}, c: {c}")


# a: 22, b: 1984, c: Doug
# a: 1984, b: Doug, c: 22   
# a: Doug, b: 22, c: 1984  