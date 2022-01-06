# Automobile Costs
# Write a program that asks the user to enter the monthly costs for the following expenses 
# incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and maintenance. 
# The program should then display the total monthly cost of these expenses, and the total annual cost of these expenses.

loan_payment = float(input("Enter the monthly loan payment of Your car: "))
insurance = float(input("Enter the monthly insurance payment of Your car: "))
gas = float(input("Enter the monthly gas expenses of Your car: "))
oil = float(input("Enter the monthly oil expenses of Your car: "))
tires = float(input("Enter the monthly tires expenses of Your car: "))
maintenance = float(input("Enter the monthly maintenance expenses of Your car: "))

def func():
    global loan_payment
    global insurance
    global gas
    global oil
    global tires
    global maintenance
    total_monthly = loan_payment + insurance + gas + oil + tires + maintenance
    total_annual = total_monthly * 12
    
    print("Your total amount of monthly automobile costs is: ", round(total_monthly,2), "EUR")
    print("Your total amount of annual automobile costs is: ", round(total_annual,2), "EUR")
func()