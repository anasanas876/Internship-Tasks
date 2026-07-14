# Task5
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculatle_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2* (self.length+self.width)
    
rec=Rectangle(50,40)
print(rec.calculatle_area())
print(rec.calculate_perimeter())
