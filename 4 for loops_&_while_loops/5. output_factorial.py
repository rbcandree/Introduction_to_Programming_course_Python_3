import random
def factorial(n):
  factorial = 1
  if n < 0:
    print("Factorial does not defined for negative integer")
  elif n == 0:
    print("The factorial of 0 is 1")
  else:
    while n > 0:
        factorial = factorial * n
        n = n - 1
  print(factorial)


numbers = list(range(1,10))

for i in range(0,5):
  number = random.choice(numbers)
  if number in numbers:
    numbers.remove(number)
  print ("Factorial of",number,"is:", factorial(number))