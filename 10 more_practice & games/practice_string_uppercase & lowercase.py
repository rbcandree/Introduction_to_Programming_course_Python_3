# Define a function called myfunc, that takes in a string, and returns a matching string 
# where every even letter is uppercase, and every odd letter is lowercase. 
# Assume that the incoming string is without numbers, spaces or punctuation and contains only letters.
# The output string can start with either an uppercase or lowercase letter, so long as letters alternate through out the string.

def myfunc(mystr):
    newstr = ''
    for letter in range(0, len(mystr), 1):
        if letter % 2 == 0:
            newstr += mystr[letter].lower()
        else:
            newstr += mystr[letter].upper()
    return newstr

mystr = "Establishment"
result = myfunc(mystr)
print(result)                   # Output: eStAbLiShMeNt