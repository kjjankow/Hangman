# HANGMAN
# Hangman came using a defined list of possible words.
# User can guess letters until letters+2 are wrong
# Eventually add graphics

import random

wordList = ["apple", "banana", "grape", "pineapple", "blueberry", "raspberry"]

word = random.choice(wordList)

print(word)
