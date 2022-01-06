# Returning Tuples for Unpacking
# We can loop through a list of tuples and "unpack" the values within them:

stock_prices = [('AAA',200),('BBB',300),('CCC',400)]
for item in stock_prices:
    print(item)                             # ('AAA', 200)
                                            # ('BBB', 300)
                                            # ('CCC', 400)

stock_prices = [('AAA',200),('BBB',300),('CCC',400)]
for item, value in stock_prices:
    print(round(value*1.1, 1))              # 220
                                            # 330
                                            # 440

# Employee of the month
work_hours = [('George',150),('Nathalie',240),('Kylie',180)]
def employee_check(work_hours):
    # Placeholders:
    current_max = 0
    employee = ''
    for name, hours in work_hours:
        if hours > current_max:
            current_max  = hours
            employee = name
        else:
            pass
    return (employee, current_max)
emp = employee_check(work_hours)
print(f'Employee of the month is: {emp[0]}, {emp[1]} hours.')       # Output: Employee of the month is: Billy, 240 hours.
# Or:
name, hours = employee_check(work_hours)
print(f'Employee of the month is: {name}, {hours} hours.')          # Output: Employee of the month is: Billy, 240 hours.