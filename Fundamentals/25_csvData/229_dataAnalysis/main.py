import pandas
data = pandas.read_csv('/Users/jihunpark/Desktop/UdaPyt/100days/25_csvData/229_dataAnalysis/squirrel_count.csv')

color_gray = len(data[data["Primary Fur Color"] == "Gray"])
color_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
color_black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [color_gray, color_cinnamon, color_black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")