# 1. Which of the following is true? The body of a while loop:
# Answer:	May or may not be executed depending on the condition.

# 2.What happens during and after the execution of this line?
#   condition = False
# Answer:   We set the value of the variable "condition" to false, and the execution of the while-loop's body is continued normally.

# 3. Which of the following is true about the while statement in Python?
# Answer:	The statements within the while block may not be executed at all.

# some example 1:
s = 0
for i in range(1,9):
    if i % 3 == 0:
        s += i
print (s)

# some example 2:
s = 0
r = range(2,6,2)
for i in r:
    s += i
print(s)

# some example 3:
r = list(range(2,8,2))
a = 0
for i in r:
    a = i
    print(a)