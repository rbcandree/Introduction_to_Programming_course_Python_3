num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

def max2(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2

maxValue = max2(num1, num2)
print(f"The maximal number is: ", maxValue)