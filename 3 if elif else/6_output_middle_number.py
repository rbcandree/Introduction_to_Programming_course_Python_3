import random
def output_middle(n1, n2, n3):

    if n1 > n2 and n1 < n3:
        print(n1)
    elif n1 > n3 and n1 < n2:
        print(n1)

    if n2 > n1 and n2 < n3:
        print(n2)
    elif n2 > n3 and n2 < n1:
        print(n2)

    if n3 > n1 and n3 < n2:
        print(n3)
    elif n3 > n2 and n3 < n1:
        print(n3)


for i in range(0,4):
    n1 = random.randint(50,150) 
    n2 = random.randint(50,150) 
    n3 = random.randint(50,150)
    print ("The numbers are:",n1,n2,n3)
    print ("The middle one is", end = " ")
    output_middle(n1,n2,n3)