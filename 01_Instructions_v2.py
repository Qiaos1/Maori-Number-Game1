"""MGN Component 1 (Instructions) v2
Allows user to input an uppercase for answers. Also prints user choice at
the end of the program"""

# Ask the user if they have played before
question = input("Have you played this game before? ").lower()

# If answer equals to Yes, Print 'Game continues'
if question == "yes" or question == "y":
    print("Game continues")

# If answer equals to No, Print 'Instructions are below
elif question == "no" or question == "n":
    print("Instructions are below")

# If answer doesn't equal to yes or no, show error
else:
    print("Please type in yes or no")

print(f"You answered {question}")
