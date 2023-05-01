"""Component 3 (Ask user for Māori name) v1
Asks the Māori name for the number generated"""

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


# Main routine
number = generate_number()
print(number)
answer = input(f"What is the Maori name for {number}?")
if answer.lower() == māori_number[number]:
    print("Yay")
else:
    print("Nope")

