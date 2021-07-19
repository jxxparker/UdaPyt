#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


print("Welcome to the tip Calculator!")

total_bill = float(input("What was the total bill? "))
tip_percent = int(input("What percentage would you like to give? 10, 12 or 15 &? "))
people_count = int(input("How many people to split the bill? "))

new_bill = (total_bill) + (total_bill * (tip_percent / 100))
bill_per_person = (new_bill / people_count)
print(f"Each person owes ${bill_per_person} ")