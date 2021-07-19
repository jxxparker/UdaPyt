# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else: 
#     do this

print("welcome to the rollercoaster! ")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("you can ride the rollerfoaster! ")
    age = int(input("What is your age? "))
    if  age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.")
    

