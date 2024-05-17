# euclid.py

# get the input numbers from the user (as strings)
a = input('What is a? ')
b = input('What is b? ')

# convert the strings to integers
a = int(a)
b = int(b)

# find the greatest common divisor
while a != b:
    print(a, b)  # see how and a and b change
    if a > b:
        a = a - b
    else:
        b = b - a

# print the result
print("greatest common divisor:", a)
