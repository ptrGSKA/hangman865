import random

# creating a list of fruits
word_list = ['grapes', 'pomegranate', 'cherry', 'pineapple', 'blueberry']

print(word_list)

word = random.choice(word_list)

print(word)

guess = input('Please enter a letter: ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
