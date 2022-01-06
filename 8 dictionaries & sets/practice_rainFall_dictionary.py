totalRain = 0.0
averageRain = 0.0
lowestRain = 0.0
highestRain = 0.0
monthLowest = ''
monthHighest = ''

rainfall = {"jan":0.0, "Feb":0.0, "Mar":0.0, "Apr":0.0, "May":0.0, "Jun":0.0, "Jul":0.0, "Aug":0.0, "Sep":0.0, "Oct":0.0, "Nov":0.0, "Dec":0.0}
for i in rainfall:
    rainfall[i] = float(input("Enter the amount of rainfall for " + i + ": "))

# values() method will return a list of values in the dictionary.
rain = rainfall.values()
# sum() method gets the total amount of rain in the rain list.
totalRain = sum(rain)
averageRain = totalRain / 12.0
lowestRain = min(rain)
highestRain = max(rain)
monthLowest = min(rainfall, key = rainfall.get)
monthHighest = max(rainfall, key = rainfall.get)

print("Total rainfall: ", format(totalRain, " .2f"))
print("Average rainfall: ", format(averageRain, " .2f"))
print(lowestRain)
print(highestRain)
print(f"The lowest amount of rain is {lowestRain} and that month is: {monthLowest}")
print(f"The highest amount of rain is {highestRain} and that month is: {monthHighest}")