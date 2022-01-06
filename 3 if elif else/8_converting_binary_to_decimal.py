import random
def output_converted(bin):
    print(int(bin, 2))

for i in range(0,4):
  bin = ""
  for j in range(0,4):
    bin += str(random.randint(0, 1))
  print ("Binary string " + bin + " is in decimal:")
  output_converted(bin)