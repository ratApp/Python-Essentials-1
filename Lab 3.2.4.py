# Lab 3.2.4
# Guess the secret number game

secret_number = 777   # Secret number chosen by the magician

print(  # Prints the welcome message
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Enter a number: "))  # Asks user to enter number to make a guess and assign to variable 'number'

while number != secret_number:   # Untill the nunmber picked by the user matches the secret number
  print("Ha ha! You're stuck in my loop\n")    # Informs user they are stuck in a loop
  number = int(input("Try again!! Enter a another number : "))    # Asks the user to try again

# If user guesses correctly
print("Well done, muggle! You are free now\n")    # Informs user they are correct and out of the continuous loop
