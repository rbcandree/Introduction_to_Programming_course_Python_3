"""
Write function shared_letters(s1, s2), which gets two strings as parameters.
The function counts and returns the number of letters that can be found in both strings. 
You can assume, that all letters in the strings are lowercase english alphabets. 
For example, if the strings were abcdabcd and cdefcdef, the function would return 2, 
since there are two shared letters, c and d.
"""
import random
def shared_letters(s1,s2):
    letter = 0
    for x in range(len(s1)):
        for y in range(len(s2)):
            if(s1[x] == s2[y]) and (s1[x] in s2):
                letter +=1
                s2 = s2.replace(s2[y],"")
                #removes already used same letters, symbols from the string - replaces all letters [y] with an empty space ""
                break
    return letter

def test():
    letters = "abcdefghijklmnopqrstuvwxyz"
    s1 = ""
    s2 = ""
    for i in range(random.randint(15,25)):
        s1 += random.choice(letters)
    for i in range(random.randint(17,23)):
        s2 += random.choice(letters)
    print ("String 1:", s1)
    print ("String 2:", s2)
    print ("Shared letters:", shared_letters(s1,s2))
    
for i in range(3):
    test()

"""
Another method through sets

def shared_letters(s1,s2):
   set_string1 = set(s1)
   set_string2 = set(s2)
   matched_characters = set_string1 & set_string2
   return str(len(matched_characters))
"""