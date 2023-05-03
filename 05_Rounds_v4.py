"""Component 5 (Rounds) v4
Puts the code into a function"""


# Function for rounds
def play_game():
    # Loop until the user says "no"
    while True:
        # Ask user whether they want to play again or not
        rounds = input("Would you like to play another round? ")

        # Convert the user input to lowercase
        rounds = rounds.lower()

        # If they say yes, output Game Continues
        if rounds == "yes":
            print("Game Continues")

        # If they say no, end game
        elif rounds == "no":
            print("Thank you for playing!")
            return  # Return from the function

        # Otherwise show error
        else:
            print("Sorry that wasn't an option. Please type yes or no")


# Starts the round function
play_game()
