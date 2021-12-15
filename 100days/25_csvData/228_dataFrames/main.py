import pandas
data = pandas.read_csv('/Users/jihunpark/Desktop/UdaPyt/100days/25_csvData/228_dataFrames/weather_data.csv')

print(type(data))
print(type(data["temp"]))

data_to_dict = data.to_dict()
print(data_to_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

average_temp = (sum(temp_list) / len(temp_list))
print(f"average temperature is {average_temp}")

mean_data = data["temp"].mean() #this is same as above which was getting average
print(mean_data)

max_data = data["temp"].max()
print(max_data)

print(data.condition) #prints the conditions
print(data.day) 

# ---get data in rows--- #monday
monday = data[data.day == "Monday"] #this prints every data that has day as monday
monday_temp = int(monday.temp)
fahrenheit_temp = monday_temp * 9/5 + 32
print(fahrenheit_temp)


# ---get the maximum temperature as in rows
max_temp_row = data[data.temp == data.temp.max()]
print(max_temp_row)

#create a datafram from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_dict_scores = pandas.DataFrame(data_dict)
print(data_dict_scores)
# data_dict_scores.to_csv("new_data.csv") #creates new csv

