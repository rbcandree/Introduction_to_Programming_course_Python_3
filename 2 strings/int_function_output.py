import random
def output_age(name_birth):
    year = name_birth[-5:]
    year1 = int(year)
    age = (2011 - year1)
    print(age) 

first = [ "John", "James", "Bill", "Arnold", "Lisa", "Ann", "Kimberly", "Monica" ]
last = [ "Smith", "Jones", "Williams", "Brown", "Wilson", "Taylor", "Johnson" ]

for i in range(3):
  name = random.choice(first) + " " + random.choice(last)
  name_age = name + ", 19" + str(random.randint(0,99))
  print ("Name and b.year:", name_age)
  print ("Age:", output_age(name_age))