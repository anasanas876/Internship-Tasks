with open ('example.txt',"r") as file:
    word="I"
    for line in file:
        if word in line:
            print(line)

