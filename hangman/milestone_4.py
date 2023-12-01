import random

class Hangman():
    '''
    The class is used to represent the instance of the Hangman game.

    Args:
        word_list (list): a given list of words where the game randomly selects a word from
        num_lives (int): the count of attempts that the player can make
        word (str): the random;y choosen element from the word_list
        word_guessed (list): initially a list, containing underscores '_' as many as the number of letters in the choosen word
        num_letters (int): the number of unique letters in the word
        list_of_guesses (list): the valid guesses entered by the player
    '''

    def __init__(self, word_list, num_lives = 5):
        '''
        The constructor initializes the attributes that necessary for the game.
        '''

        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def __check_guess(self, guess):
        '''
        The function is verifying if the letter is in the choosen random word.

        Args:
            guess (str): user input
        Returns:
            N/A
        '''

        # Convert guess into lowercase
        guess = guess.lower()

        # Verifying if the letter is in the choosen random word an appending the guess to the word_guessed list.
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for pos in range(0,len(self.word)):
                if self.word[pos] == guess:
                    self.word_guessed[pos] = guess
            self.num_letters -= 1

        # Called if the guessed letter not in the word.
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')


    def ask_for_input(self):
        '''
        The function is asking for a user input.

        Args:
            guess (str): user input
        Returns:
            N/A
        '''
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
                self.__check_guess(guess)
                self.list_of_guesses.append(guess)


word_list = ['grapes', 'pomegranate', 'cherry', 'pineapple', 'blueberry']
game = Hangman(word_list)
game.ask_for_input()