"""MNG base component
Components added after they have been tested and created"""


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
