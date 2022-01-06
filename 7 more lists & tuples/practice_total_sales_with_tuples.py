"""
Design a program that asks the user to enter a stores sales for each day of the week. 
The amounts should be stored in a list.
Use a loop to calculate the total sales for the week and display the result.
"""

totalSales = 0.00
salesList = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
weekdayTuple = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

for i in range(7):
    salesList[i] = float(input("Enter the store's sales for " + weekdayTuple[i] + " : "))

totalSales = sum(salesList)
print("Total sales for the week: ", format(totalSales, " .2f"))