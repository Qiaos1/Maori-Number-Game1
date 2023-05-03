"""Component 5 (Rounds) v2
Solves the problem of upper cases and also allows abbreviations.
Also states user choice at the end"""

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

# Otherwise show error
else:
    print("Sorry that wasn't an option")
