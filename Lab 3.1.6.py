# Lab 3.1.6

# Scenario
# Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.

# Don't create any if blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.


n = int(input("Enter a whole number:"))    # Assign an input as an integer

if n >= 100:             # If n is greater than or equal to 100
  print("True")          # Prints "True"
else:                    # Otherwise (If less than 100)
  print("False")         # Prints "False"