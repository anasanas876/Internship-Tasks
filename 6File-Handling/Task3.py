# Task 3
user_name=input('Enter  your name')
with open ("example.txt","a") as file:
    file.write(user_name)
    print("Content saved successfully")
    