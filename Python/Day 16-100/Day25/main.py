# # # import csv
# # #
# # # with open("weather_data.csv", "r") as data_file:
# # #     data = csv.reader(data_file)
# # #     temperatures = []
# # #     for row in data:
# # #         if row[1] != "temp":
# # #             temperatures.append(int(row[1]))
# # #
# # # print(temperatures)
# #
# # import pandas
# #
# # data = pandas.read_csv("weather_data.csv")
# # tempe = data["temp"]
# # # print(tempe)
# # #
# # # mean = tempe.mean()
# # # print(mean)
# # # print(data.temp.max())
# # # print(data[data.temp == data.temp.max()])
# # monday = data[data.day == "Monday"]
# # mondaytemp = monday.temp
# # F = mondaytemp * (9/5) +32
# # print(F)
# import pandas
#
# data_dict = {
#     "students" : ["Amy", "James", "Angela"]
#     "scores" : [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260531.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])

red = len(data[data["Primary Fur Color"] == "Cinnamon"])

black = len(data[data["Primary Fur Color"] == "Black"])

print(black, gray, red)

data_frame = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [gray, red, black],
}

data = pandas.DataFrame(data_frame)
data.to_csv("squirrel_count.csv")