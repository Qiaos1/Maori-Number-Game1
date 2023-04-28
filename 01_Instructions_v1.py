"""MNG Component 1 (Instructions) v1
Asks whether the user has played before. Also accepts abbreviations"""

# Ask the user if they have played before
question = input("Have you played this game before? ")

# If answer equals to Yes, Print 'Game continues'
if question == "yes" or question == "y":
    print("Game continues")

# If answer equals to No, Print 'Instructions are below
elif question == "no" or question == "n":
    print("Instructions are below")

# If answer doesn't equal to yes or no, show error
else:
    print("Please type in yes or no")
