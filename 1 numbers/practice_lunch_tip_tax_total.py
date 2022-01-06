lunch_price = float(input("Please, do not use letters or comma. Enter the price of Your lunch:"))
lunch_price = float(lunch_price)
price = "{0:.2f}".format(lunch_price)
tip = "{0:.2f}".format(float((lunch_price * 15) / 100))
tax = "{0:.2f}".format(float((lunch_price * 7) / 100))
total_price = "{0:.2f}".format((lunch_price + (lunch_price * 15) / 100) + (lunch_price * 7) / 100)

print("Amount of a tip is: ", str(tip), "EUR")
print("Amount of a tax is: ", str(tax), "EUR")
print("Total price is: ", str(total_price), "EUR")

# Or:
"""
lunch_price = float(input("Please, do not use letters or comma. Enter the price of Your lunch:"))
tip = lunch_price * .15
tax = lunch_price * .07
total_price = (lunch_price + tax + tip)

print("Amount of a tip is: ", round(tip,2), "EUR")
print("Amount of a tax is: ", round(tax,2), "EUR")
print("Total price is: ", round(total_price,2), "EUR")
"""