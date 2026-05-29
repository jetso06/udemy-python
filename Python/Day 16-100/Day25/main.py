# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         temp = int(row[1])
#         temperatures.append(temp)
# print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
#temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
F = (monday_temp * 1.8) + 32
#monday.update(monday.temp = monday_temp)
print(F)