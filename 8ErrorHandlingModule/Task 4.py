# Task 4
class ValueLessThanZero(Exception):
    pass
try:

    age=int(input("Enter your age"))
    if age<0:

     raise ValueLessThanZero("The value can not be less than zero")
except ValueLessThanZero as error:
    print(f"Caught a custom error:{error}")
else:
   print(f"Your age is{age}") 
