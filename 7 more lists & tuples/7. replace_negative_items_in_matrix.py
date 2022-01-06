"""
Write a procedure replace_negatives(matrix), which receives a matrix with integer items as an argument.
The function replaces all negative items in the matrix with their absolute values 
(for example -1 is replaced with 1 and -7 with 7).

*method abs() , returns absolute value of integer, for example abs(-1) = 1
"""
import random
# next line generates a random number
# and assigns it to variable n1
n1 = random.randint(50,150) 
def replace_negatives(matrix):
    for row in matrix:
        for i in range(len(row)):
            if row[i] < 0:
                row[i] = abs(row[i])
    return
    
def test():
    m = []
    size = random.randint(4,7)
    for i in range(size):
        m.append([0] * size)
        for j in range(size):
            m[i][j] = random.randint(-10,10)
    print ("Matrix before:")
    output_matrix(m)
    print ("")
    
    replace_negatives(m)
    print ("Matrix after:")
    output_matrix(m)
    
def output_matrix(m):
    for row in m:
        print (row) 

test()      