import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
#
# #Equivalent to:
# average = data["temp"].mean()
# print(average)
#
# #Get data in Columns
# print(data["condition"])
# print(data.condition)
#
# #Get data in Row
# print(data[data.temp  == data["temp"].max()])
# print(data[data.temp == 14])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# temp_in_fahrenheit = monday_temp * 9/5 + 32
# print(temp_in_fahrenheit)
#
# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Gosho", "Pesho", "Ivan"],
#     "scores": [85, 79, 67]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241025.csv")

gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrel_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")