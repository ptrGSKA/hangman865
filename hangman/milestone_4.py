import random

class Hangman():

    def __init__(self, word_list, num_lives = 5):

        # Initializing attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):

        # Convert guess into lowercase
        guess = guess.lower()

        # Verifying if the letter is in the choosen random word an appending the guess to the word_guessed list.
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for pos in range(0,len(self.word)):
                if self.word[pos] == guess:
                    self.word_guessed[pos] = guess
            self.num_letters -= 1
        
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')


    def ask_for_input(self):

        while True:

            # Ask user for input
            guess = input('Please enter a letter:   ')

            # Verifying the authenticity of the letter.
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
                continue
            
            # Determine whether the letter has been guessed before.
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
                continue
            
            # Function call to validate the letter and appending the guess to the list_of_guesses.
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


word_list = ['grapes', 'pomegranate', 'cherry', 'pineapple', 'blueberry']
game = Hangman(word_list)
game.ask_for_input()