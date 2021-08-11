Variadic keyword parameters

a parameter of the form **name such as **kwargs, in a function signature introduces a variadcic keyword parameter. 

def print_my_arguments(a, b=1, **c):
    print(f"a={a}, b={b}, c={c}")

print_my_arguments(2)                      # a=2, b=1, c={}
print_my_arguments(2, x=7)                 # a=2, b=1, c={'x': 7}
print_my_arguments(2, x=7, y=1)            # a=2, b=1, c={'x': 7, 'y': 1}
print_my_arguments(2, x=7, y=1, z=8)       # a=2, b=1, c={'x': 7, 'y': 1, 'z': 8}
print_my_arguments(2, x=7, y=1, z=8, b=2)  # a=2, b=2, c={'x': 7, 'y': 1, 'z': 8}
print_my_arguments(2, x=7, b=2, y=1, z=8)  # a=2, b=2, c={'x': 7, 'y': 1, 'z': 8}

Note that C is our variadic keyword parameter, and it contains a dictionary of the excess positionally supplied arguments.

