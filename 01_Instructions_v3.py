"""MGN Component 1 (Instructions) v3
Turns the code in v2 into a loop to make testing easier"""

question = ""
while question != "S":
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
