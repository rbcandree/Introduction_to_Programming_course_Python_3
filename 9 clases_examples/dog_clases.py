#
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        #this method will printthe dog information
        print(f"My dog is {self.name} and my dog age is {self.age} years old.")

    def sit(self):
        print(f"{self.name} is now sitting.")

    def rollOver(self):
        print(f"{self.name} rolled over.")

mydog = Dog("Zooz", 6)
yourdog = Dog("Coco", 4)
herdog = Dog("Zooooooooooooooz", 6)
hisdog = Dog("Cocooooooo", 4)

mydog.print()
mydog.sit()

yourdog.print()
yourdog.rollOver()

herdog.print()
herdog.sit()
herdog.rollOver()

hisdog.print()