num1 = 11
num2 = num1

print("Before value is updated")
print("num1 =", num1)
print("num2 = ", num2)

num1 = 22

print("After value is updated")
print("num1 =", num1)
print("num2 = ", num2)


dict1 = {
    "value": 11
}

dict2 = dict1

print("before value is updated")
print("dict1 =", dict1)
print("dict2", dict2)

dict1["value"] = 22

print("After value is updated")
print("dict1 =", dict1)
print("dict2", dict2)

dict3 = {
    "value": 57
}

dict2 = dict3
print("dict2", dict2)