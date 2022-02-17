import random

names_string = input("Give me everones names ")
names = names_string.split(", ")
print(names)

num_items = len(names)
# print(num_items)

random_choice = random.randint(0,num_items - 1)

person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to pay")