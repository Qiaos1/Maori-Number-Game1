"""Component 5 (Rounds) v1
Generates rounds and asks user whether they want to carry on playing or not"""

# Ask user whether they want to play again or not
rounds = input("Would you like to play another round?")

# If they say yes, output Game Continues
if rounds == "yes":
    print("Game Continues")

# If they say no, end game
elif rounds == "no":
    print("Thank you for playing!")

# Otherwise show error
else:
    print("Sorry that wasn't a option")
