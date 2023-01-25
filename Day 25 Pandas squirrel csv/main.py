# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as file:
#     # Read files
#     data = csv.reader(file)
#     temperatures = []
#     # Skip headers
#     next(data)
#     # Print each row in file, Row is an object
#     for row in data:
#         print(row)
#         temp = row[1]
#         temperatures.append(int(temp))
#     print(temperatures)
#

import pandas
# data = pandas.read_csv("weather_data.csv")
# Iterate to "temp" category in Dataframe
# temperatures = data["temp"]
# print(data)
# print(temperatures)

# pandas to Dict
# data_dict = data.to_dict()
# print(data_dict)

"""Series is the entirety of a row and/or column in the Dataframe, one dimensional"""
# # Series to list
# temp_list = data["temp"].to_list()
# # Find average
# print(round((sum(temp_list) / len(temp_list)), 2))
# another way
# print(data["temp"].mean())
#
# # Find maximum value
# print(data["temp"].max())
#
# # Get data from columns
# print(data["condition"]) or print(data.condition)

# Get data from Rows
# print(data[data.day == "Monday"])
#
# # Get data from row with Max Temp
# print(data[data.temp == data.temp.max()])

# monday = (data[data.day == "Monday"])
# print(monday.condition)
#
# temperature = monday.temp
# f_temp = ((temperature * 9/5) + 32)
# print(f_temp)


# Create Dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# # Dataframe to CSV file
# data.to_csv("new_data.csv")


# Squirrel Census Count
GRAY = 0
CINNAMON = 0
BLACK = 0
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey, cinnamon, black]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("Fur_color.csv")


fur_color = data["Primary Fur Color"]
for color in fur_color:
    if color == "Gray":
        GRAY += 1
    elif color == "Cinnamon":
        CINNAMON += 1
    else:
        BLACK += 1

data_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [GRAY, CINNAMON, BLACK]
}

print(data_dict)

fur_data = pandas.DataFrame(data_dict)
fur_data.to_csv("fur_data.csv")

""" USA State Game """
