height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

int_height = float(height)
int_weight = float(weight)

bmi =  (int_weight) / (int_height * int_height)
int_bmi = int(bmi)
str_bmi = str(int_bmi)
print("your bmi is " + str_bmi)