"""Component 2 (Generate Random Number) v1
Generates random number between 1 and 10"""

import random

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# Testing loop to generate 10 numbers
for item in range(10):
    number = random.choice(numbers)
    print(number, end='\t')  # Makes the numbers easier to screenshot
