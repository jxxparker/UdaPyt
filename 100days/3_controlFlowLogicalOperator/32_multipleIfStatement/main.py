# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do c

print("welcome to the rollercoaster! ")
height = int(input("what is your height in cm? "))

bill = 0
if height >= 120:
    print("you can ride the rollerfoaster! ")
    age = int(input("What is your age? "))
    if  age < 12:
        bill = 5
        print("child tickets $5 ")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7 ")
    else:
        bill = 12
        print("adult tickets are $12 ")
    
    wants_photo = input("Do you want a photo taken? Yes or No ").lower()
    if wants_photo == "yes":
        bill = bill + 3
    
    print(f"your final bill is {bill}")


    
else:
    print("Sorry, you have to grow taller before you can ride.")
    

