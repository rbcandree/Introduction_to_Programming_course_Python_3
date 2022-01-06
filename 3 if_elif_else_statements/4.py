number = 125.0
min = 100
max = 150
if number > min and number < max:
    number = number + 25
    print(number)

if number <= min or number >= max:
    number = number / 2
    print(number)

else:
    number = number * 2
    print(number)
 
if number < 100 and number % 5 == 0:
    number = number / 5
    print(number)