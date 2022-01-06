import random
def first_upper(word):
    my_string = word
    b = my_string[0]
    c = my_string[1:]
    print(b.upper() + c.lower())

words = [ "quick", "letters", "apple", "appreciates", "programming", "zippers", "key", "paragraph", "admin", "student", "teacher", "compare", "dog", "designing", "development", "studies", "run", "dynamic", "fox", "place" ]

for i in range(0,4):
  word = random.choice(words)
  print ("The word is: " + word)
  print ("1st, middle and last letter are:")
  first_upper(word)