#3.2.11   LAB   The continue statement  the Pretty Vowel Eater
#user_word = input("Enter a word: ")

#user_word = user_word.upper()   # Convert to uppercase

#for letter in user_word:
#    if letter == ("A" or "E" or "I" or "O" or "U"):
#        continue
#    else:
#        print(letter)


# Prompt the user to enter a word
user_word = input("Input your name: ") # creating a variable for user's name 

# and assign it to the user_word variable.
user_word = user_word.upper() # Converting to uppercase

word_without_vowels = ""

for letter in user_word: 
    if letter in "AEIOU":continue
    else:
        word_without_vowels += letter # adding the letters to the word
print(word_without_vowels)

