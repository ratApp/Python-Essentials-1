
# 3.1.10   LAB   Comparison operators and conditional execution
# Scenario
# Spathiphyllum, more commonly known as a peace lily or white sail plant, is one of the most popular indoor houseplants that filters out harmful toxins from the air. Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.

# Imagine that your computer program loves these plants. Whenever it receives an input in the form of the word Spathiphyllum, it involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"

# Write a program that utilizes the concept of conditional execution, takes a string as input, and:

# prints the sentence "Yes - Spathiphyllum is the best 
# plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
# Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!


n = input("Enter a name of plant: ")

if n == "Spathiphyllum":    # If name is entered correctly
  print("Yes - Spathiphyllum is the best plant ever!")   # Gives positive feedback
elif n == "spathiphyllum":   # If name is correct but first letter is not capital
  print("No, I want a big Spathiphyllum!")  # Gives negative feedback
else:  # If wrong name is given
  print("Spathiphyllum! Not ",n,"!") # Corrects the name with the name entered
