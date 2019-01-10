# HANGMAN
# Hangman came using a defined list of possible words.
# User can guess letters until letters+2 are wrong
# Eventually add graphics

import random

wordList = ["apple", "banana", "grape", "pineapple", "blueberry", "raspberry"]

word = random.choice(wordList)      # Selects a random word from wordList and assigns to word

print(word)  # Check to see set up is working

print('Guess the fruit word!')

for i in word:
    print('_', end = " ")   # Shows missing letters from the word
print()                     # Adds extra line break

lettersGuessed = ''
chances = len(word)+2       # Sets chances to guess to length of the word + 2
correct = 0                 # initializes correct guesses to 0 at start of the game

guess = str(input('Enter a letter to guess'))
print()

if guess in word:
    lettersGuessed += guess

for char in word:
    if char in lettersGuessed:
        print(char, end=" ")
        correct += 1
    else:
        print('_', end=" ")

print('Game over!')



