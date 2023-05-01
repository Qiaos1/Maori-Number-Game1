"""Component 2 (Generate Random Number) v2
Turns version 1 into a function"""

import random


# Function to generate random number between 1 and 10
def generate_number():
    return random.sample(range(1, 11), 10)


# Main Routine
ten_numbers = generate_number()
print(ten_numbers)
