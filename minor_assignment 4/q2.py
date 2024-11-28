# Define the rotate function
def rotate(arg1, arg2, arg3):
    return arg2, arg3, arg1

# Initialize variables
a, b, c = 'Doug', 22, 1984

# Call the function three times, unpacking the result
for i in range(3):
    a, b, c = rotate(a, b, c)
    print(f"a: {a}, b: {b}, c: {c}")
