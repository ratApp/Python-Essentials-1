#3.2.10   LAB   The continue statement  the Ugly Vowel Eater


user_word = input("Enter a word: ")

user_word = user_word.upper()   # Convert to uppercase

#for letter in user_word:
#    if letter == ("A" or "E" or "I" or "O" or "U"):
#        continue
#    else:
#        print(letter)


for letter in user_word:
    if letter in "AEIOU":continue
    else:
        print(letter)


