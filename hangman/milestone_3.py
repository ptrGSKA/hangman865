import random

# List of fruits
word_list = ['grapes', 'pomegranate', 'cherry', 'pineapple', 'blueberry']

# Selecting randomly an element from the word_list
word = random.choice(word_list)

def check_guess(guess):

    # Convert guess into lowercase
    guess = guess.lower()

    # Check whether the user inputed guess is in the randomly choosen word
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():

    # The loop checks the validity of the guess, allowing only single alphabetic
    while True:

        # Ask user for input
        guess = input('Please enter a letter:   ')

        # Verifying the authenticity of the letter.
        if len(guess) == 1 and guess.isalpha():
            #print('Good guess!')
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
            continue
    check_guess(guess)

ask_for_input()
