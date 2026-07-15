# Task 1
try:
    number=int(input("Enter a number"))
    result=10/number
except ZeroDivisionError:
    print("Number can not be divided by zero")
else:
    print(f"The result is:{result}")

     