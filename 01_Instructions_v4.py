"""MGN Component 1 (Instructions) v4
Turns the code in v3 into a function"""


# Function for Instructions...
def instructions(question):
    while True:

        # Ask the user if they have played before
        question = input(question).lower()

        # If answer equals to Yes, Print 'Game continues'
        if question == "yes" or question == "y":
            answer = "Yes"
            return answer

        # If answer equals to No, Print 'Instructions are below
        elif question == "no" or question == "n":
            answer = "No"
            return answer

        # If answer doesn't equal to yes or no, show error
        else:
            print("Please type in yes or no")


# Main Routine
show_instructions_below = instructions("Have you played this game before?")
print(f"You answered {show_instructions_below}")
