#variables

x = 47320

#namespaces
# - a namespace is an associative mapping from names to objects

#variable assignment
# - assigning from a variable does not copy an object
# - instead, it adds another reference to the same object

x = "Hello, there"
y = x

print(y)
print(x is y) #true

print(id(x))

print(locals()['x'])

#recap: objects, names and namespaces
# everything is an object
# an object has a type and identity
# use == to compare value and is to compare identities
