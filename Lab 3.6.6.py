#3.6.6   LAB   Operating with lists ‒ basics
#Scenario
#Imagine a list ‒ not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.

#Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.

#Note: assume that the source list is hard-coded inside the code ‒ you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.

#Hint: we encourage you to create a new list as a temporary work area ‒ you don't need to update the list in situ.

#We've provided no test data, as that would be too easy. You can use our skeleton instead.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

u_list = []   # Create an empty list

for number in my_list:         # Iterate over the main list
    if number not in u_list:   # If the number is not in the u_list
        u_list.append(number)  # Add the number
print("The list with unique elements only:\n", u_list)  # Print list with unique numbers
print("The list with original elements:\n", my_list)    # Print the original list
