# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_h = float(height)
int_w = float(weight)

bmi = int_w / (int_h * int_h)
print(bmi)