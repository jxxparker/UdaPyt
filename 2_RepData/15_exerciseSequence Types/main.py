#in the slicing section, fill out the code with the correct slice values to get the proper outputs

# Slicing
hello = 'Hello, world!'

a = hello[0].upper()  # Turn me into 'H'
b = hello[-2]  # Turn me into 'd'
c = hello[1:5]  # Turn me into 'ello'
d = hello[7:13]  # Turn me into 'world!'
e = hello[::2]  # Turn me into 'Hlo ol!'
f = hello[::-1]  # Turn me into '!dlrow ,olleH'

#in the manipulating string section, write the make_palindrome function to convert a string into a palindrome whose prefix is the given string. can you find the shortest possible palindrome.

def make_palindrome(s):
    print(s + s[::-1])
    
    
make_palindrome(['jam', "jih", 'hi'])

#In the # Manipulating Lists and Tuples section, write the add_layer function to add a layer to a growing representation of Pascal's triangle.

#In the # Manipulating Lists and Tuples section, write the add_layer function to add a layer to a growing representation of Pascal's triangle.


def add_layer(triangle):
    last = triangle[-1]  # The most recent row of Pascal's triangle.
    row = []  # Build up the next row.
    for left, right in zip(last + (0,), (0,) + last):
        row.append(left + right)
    triangle.append(tuple(row))

