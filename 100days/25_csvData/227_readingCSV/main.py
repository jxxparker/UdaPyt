# with open('/Users/jihunpark/Desktop/UdaPyt/100days/25_csvData/227_readingCSV/weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures =  []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("/Users/jihunpark/Desktop/UdaPyt/100days/25_csvData/227_readingCSV/weather_data.csv")
print(data)