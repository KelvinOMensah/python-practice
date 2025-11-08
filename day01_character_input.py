# A program that asks the user to enter their name and age 
# Prints out the message addressed to them and tells the user when he/she will turn 100 years old

name = input("Enter your name: ")

birth_year = int(input("Enter birth year: ")) 

current_age = 2025 - birth_year

new_age = birth_year + 100

print(f"Hello {name}")

print(f"You were born in {birth_year} and you are {current_age} years old")

print(f"You will be 100 years in the year {new_age}")


