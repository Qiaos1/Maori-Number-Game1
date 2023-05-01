"""Component 4 (Feedback on answers) v1
Based on Component 3. Gives appropriate feedback on answers."""


import random


# Māori numbers from one to ten
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


# Function to play the Māori Number Game
def māori_game():
    while True:
        number = generate_number()
        print(number)
        answer = input(f"What is the Maori name for {number}? (Type Exit to"
                       f" stop playing)")
        if answer.lower() == "exit":
            break
        elif answer.lower() == māori_number[number]:
            print(f"Congratulations! You are correct!")
        else:
            print(f"Sorry, you are incorrect")


# To start the game
māori_game()
