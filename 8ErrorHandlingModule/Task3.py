# Task 3
try:
    with open("new.txt", "r"):
        print("File found.")
except FileNotFoundError:
    print("There is no file named new.txt")