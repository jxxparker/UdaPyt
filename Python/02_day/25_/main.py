# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_age = int(age)
year_left = 90 - int_age
days_left = year_left * 365
weeks_left = year_left * 52
months_left = year_left * 12

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")