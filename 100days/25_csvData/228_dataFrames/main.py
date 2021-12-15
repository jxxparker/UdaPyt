import pandas

data = pandas.read_csv("/Users/jihunpark/Desktop/UdaPyt/100days/25_csvData/227_readingCSV/weather_data.csv")
# print(type(data))
print(type(data["temp"]))