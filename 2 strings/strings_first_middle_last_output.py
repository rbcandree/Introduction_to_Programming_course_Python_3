import random
def output(word):
    
    middle = len(word) // 2
    my_string = word
    print(my_string[0])
    print(my_string[middle])
    print(my_string[-1])

words = [ "quick", "letters", "apple", "appreciates", "programming", "zippers", "key", "paragraph", "admin", "student", "teacher", "compare", "dog", "designing", "development", "studies", "run", "dynamic", "fox", "place" ]

for i in range(0,4):
  word = random.choice(words)
  print ("The word is: " + word)
  print ("1st, middle and last letter are:")
  output(word)