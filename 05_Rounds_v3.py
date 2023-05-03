"""Component 5 (Rounds) v3
Puts the code into a loop to make testing easier"""

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
        break  # Exit the loop

    # Otherwise show error
    else:
        print("Sorry that wasn't an option")
