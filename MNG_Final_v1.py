"""MNG final version"""

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
        answer = input(
            f"What is the Maori name for {number}?")
        if answer.lower() == "exit":
            break
        elif answer.lower() == māori_number[number]:
            print(f"Congratulations! You are correct!")
        else:
            print(
                f"Sorry, you are incorrect. The correct answer"
                f" is {māori_number[number]}")

        play_again = input(
            "Would you like to play another round? (Type Yes or No)").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Please type Yes or No.").lower()

        if play_again == "no":
            break


# Function to show instructions
def instructions():
    print("* * * * How to play * * * *")
    print()
    print(
        "Once it generates a random digit, you must put the Māori"
        " name of the number next to the digit.")
    print()
    print("It will tell you whether you are right or wrong at "
          "the end of each round")
    print()
    print("Have fun playing!")


# Function for rounds
def play_game():
    # Loop until the user says "no"
    while True:
        # Ask user whether they want to play again or not
        rounds = input("Are you sure you want to leave this game? (Type yes "
                       "if you want to leave the game and no if you want to"
                       " carry on playing) ")

        # Convert the user input to lowercase
        rounds = rounds.lower()

        # If they say yes, output Game Continues
        if rounds == "yes":
            print("Thank you for playing!")
            return  # Return from the function

        # If they say no, end game
        elif rounds == "no":
            print("Game Continues")

            # Call the māori_game function to play another round
            māori_game()

        # Otherwise show error
        else:
            print(
                "Sorry that wasn't an option. Please type yes or no")


# Main Routine
played_before = input(
    "Have you played this game before? (Type Yes or No)").lower()
while played_before not in ["yes", "no"]:
    played_before = input("Invalid input. Please type Yes or No.").lower()

if played_before == "no":
    instructions()

māori_game()
play_game()
