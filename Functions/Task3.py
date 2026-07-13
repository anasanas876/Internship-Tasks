# Task 3
def count_vowels(user_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in user_string:
        if char in vowels:
            count += 1

    return count

user_string = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_string))