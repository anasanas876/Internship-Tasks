# Task 3
class Animal:
    def __init__(self,name):
        self.name=name
    
class Dog(Animal):
    
    def sound(self):
        print(self.name, "barks")

class Cat(Animal):
    def sound(self):
        print(self.name, "mewos")

dog1=Dog('buddy')
dog1.sound()
cat1=Cat('pretty')
cat1.sound()