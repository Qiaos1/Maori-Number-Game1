"""MNG base component v2
Adds Component 3 and 4 to the base component"""


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
            print(f"Sorry, you are incorrect. The correct answer is"
                  f" {māori_number[number]}")


# Function for question
def question(question_):
    while True:

        # Ask the user if they have played before
        question_ = input(question_).lower()

        # If answer equals to Yes, Print 'Game continues'
        if question_ == "yes" or question_ == "y":
            answer = "Yes"
            return answer

        # If answer equals to No, Print 'Instructions are below
        elif question_ == "no" or question_ == "n":
            answer = "No"
            return answer

        # If answer doesn't equal to yes or no, show error
        else:
            print("Please type in yes or no")


# Function to show instructions
def instructions():
    print("* * * * How to play * * * *")
    print()
    print("Once it generates a random digit, you must put the Māori name of "
          "the digit next to the digit.")
    print()
    print("Press <enter> to start the game")
    print()
    print("When you want to stop playing just type 'Exit'")
    print()
    print("Have fun playing!")


# Main Routine
played_before = question("Have you played this game before? ")
print(f"You answered {played_before}")
if played_before == "No":
    instructions()
else:
    print("Game continues")
māori_game()
