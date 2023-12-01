# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

# Table of Contents
1. [Description](#description)
    - [Milestone 1](#milestone-1)
    - [Milestone 2](#milestone-2)
    - [Milestone 3](#milestone-3)
    - [Milestone 4](#milestone-4)
    - [Milestone 5](#milestone-5)
2. [Installation](#installation)
3. [How to use](#how-to-use)
4. [File structure](#file-structure)
5. [Licence](#licence)

# Description

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 1

Setting up the github repository for the Hangman project and cloning the repository for local use.

## Milestone 2

Creating the first parts of the game.
Construct a record and request the user to provide an entry that is verified to be a single alphabetical character.

## Milestone 3

In this phase of the project, two functions were established. The initial function prompts the user for input,
while the second function dynamically verifies the accuracy of the user's guess. 

## Milestone 4

Created the Hangman game class with initialized attributes and two methods.

check_guess method: it converts the user input into lower case than Vverifies if the letter is in the choosen random word,
                    and appending the guess to the word_guessed list.

ask_for_input method: asking for user input and verifies the validity of the guess or the letter has been guessed before.
                    If the letter passes all checks it calls the check_guess_method and appends the guess to the list_of_guesses.

## Milestone 5

The finals steps were coded in this part of the project.
The play_game function has been added to the file.

play_game function: The function operates until the player either emerges victorious or faces defeat.
                    The conditions are evaluated after every step and a decision is made accordingly. 

# Installation 

Follow the steps to install the game:

1. Clone the github repository by typig in the Command Line Interface ```git clone [git_repository_url]``` on either operating system.
2. Navigate to the folder where the repository was cloned and in the hangman folder open a terminal/shell or alternatively navigate to the folder using the shell.
3. Type the command  ```python3 hangman.py``` to start the game.

# How to use

Once the game begins, it is played within the CLI environment. 
The user is prompted by the game to provide an input in the form of a letter, and the game persists until the word is correctly guessed
or the player exhausts all of their lives.
If the guessed letter is invalid, the game will inform the user and prompt for another letter instead.
The system keeps track of all the attempts made to ensure that no letter is repeated.

# File structure

The files for the game can be found in the hangman folder.

- hangman
    - milestone_2.py
    - milestone_3.py
    - milestone_4.py
    - milestone_5.py
    - hangman.py
- README.md

# Licence

CC0 1.0 Universal - see Licence.txt