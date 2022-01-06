a = 3
b = 5
a = b - 1
b = b + a + a % 3
a = a % 4
b = b - 3
s = "Python Program"
if s[a] == s[b]:
    print(s)