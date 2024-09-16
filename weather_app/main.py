# # import csv
# #
# # with open("weather_data.csv") as weather_info:
# #     weather_data = csv.reader(weather_info)
# #     temperatures = []
# #     for row in weather_data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
#
# def cel_convert(cel):
#     far = (cel * (9 / 5) + 32)
#     return far
#
#
# data = pandas.read_csv('weather_data.csv')
# # temp_list = data['temp'].to_list()
# # avg_temp = round(sum(temp_list)/len(temp_list))
# # print(avg_temp)
# # print(data['temp'].mean())
# # print(data['temp'].max())
# #
# # print(data[data.temp == data.temp.max()])
#
# monday = (data[data.day == 'Monday'])
# print(cel_convert(monday['temp']))

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = data[data['Primary Fur Color'] == "Gray"]
cinnamon_squirrels = data[data['Primary Fur Color'] == "Cinnamon"]
black_squirrels = data[data['Primary Fur Color'] == "Black"]

squirrel_dict = {
    'Color': ("Gray", "Cinnamon", "Black"),
    'Counts': (gray_squirrels['Unique Squirrel ID'].count(),
               cinnamon_squirrels['Unique Squirrel ID'].count(),
               black_squirrels['Unique Squirrel ID'].count()),
}



# print(data[data.primary_fur_color == "Gray"].count())


# squirrel_dict =

squirrel_data = pandas.DataFrame(squirrel_dict)

squirrel_data.to_csv('squirrel_count.csv')
