#tuples
#A tuple is an immutable sequence of arbitrary data.

# pet = (1, 'dog')
# print(pet)

# fish = (1, 2, "red", "blue")
# print(fish[:2])

a, b = 0, 1
for i in range(10):
    print(i, a)
    a, b = b, a + b