"""
Write a function even_value_set(list1, list2, list3), which receives three lists containing integer items as arguments. 
The function creates and returns a set that contains all items with even value from all three lists.
"""
import random

def even_value_set(list1, list2, list3):
    even_num = set()
    num_list = list(list1 + list2 + list3)
    for n in num_list:
        if n % 2 == 0:
            even_num.add(n)
        else:
            pass 
    return even_num

def test():
    l = [[],[],[]]
    
    for i in range(3):
        for j in range(random.randint(7,14)):
            l[i].append(random.randint(1,35))
        print ("List" + str(i + 1) +":",l[i])
        
    print ("")
    s = even_value_set(l[0],l[1],l[2])
    print ("Return type:", str(type(s)).replace("<","").replace(">",""))
    print ("Set with even values only:", end = "")
    print (set(sorted(list(s))))
    
test()