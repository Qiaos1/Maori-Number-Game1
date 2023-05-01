"""Component 3 (Ask user for Māori name) v2
Turns version 1 into a loop to make testing easier"""

import random


# Maori numbers from one to ten
māori_number = {
    1: "tahi",
    2: "rua",
    3: "toru",
    4: "wha",
    5: "rima",
    6: "ono",
    7: "whitu",
    8: "waru",
    9: "iwa",
    10: "tekau"}


# Function to generate random number between 1 and 10
def generate_number():
    return random.randint(1, 10)


# Main Routine
while True:
    number = generate_number()
    print(number)
    answer = input(f"What is the Maori name for {number}? (Type Exit to stop "
                   f"playing)")
    if answer.lower() == "exit":
        break
    elif answer.lower() == māori_number[number]:
        print("Correct")
    else:
        print("Incorrect")
