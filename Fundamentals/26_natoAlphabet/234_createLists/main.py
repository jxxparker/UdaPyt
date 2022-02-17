#list comprehension

numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "ghoney"
new_list = [letter for letter in name]
print(new_list)

range_list = [num * 2 for num in range(1,5)]
print(range_list)

names = ["ghoney", "Jordan", "James", "Bryant", "Jihun", "Kevin"]
short_names = [name for name in names if len(name) < 6]
print(short_names)

# --------------
upper_names = [name.upper() for name in names] 
print(upper_names)