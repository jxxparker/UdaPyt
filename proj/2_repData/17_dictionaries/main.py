#dictionary

# #mapping

# empty = {}
# print(type(empty))

# a = {"one": 1, "two": 2, "three":3}
# print(a)
# a["one"] = 11
# print(a)

# temps = {'CA': [101, 115, 108], 'NY': [98, 102]}

# print(temps.get('CA') ) 
# print(temps.get('KY') )

# ky_temps = temps.get('KY', [])
# print(ky_temps)
# num_observations = len(ky_temps)
# print(num_observations)


#removing element
d = {"one": 1, "two": 2, "three": 3}

print(d)
d.pop("three")
print(d)

d.popitem() #deletes last item 
print(d)

#note that iterating over a dictionary produces a elements from its collection of keys - if you want to loop over key: value pairs, youll likely use the following pattern:
