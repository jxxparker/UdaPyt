weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

bmi = (weight) / (height * height)
print(bmi)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi > 18.5 and bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight")
elif bmi > 25 and bmi < 30:
    print(f"Your bmi is {bmi}, you are slightly overweight")
elif bmi > 30 and bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
elif bmi > 35:
    print(f"your bmi is {bmi}, you are clinically obese")
else:
    print("please insert a proper weight and height")
