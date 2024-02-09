import hangman_graphics
import word_list
import random

# Constants
WINNER_MESSAGE = "You win!"
LOSER_MESSAGE = "You lose!"
MAX_TRIES = 6

# game variables
letters_guessed = []
tries = 0
hangman_graphics.show_title()
word_to_guess = random.choice(word_list.word_list).lower()

# create a list for player's guessing progress
player_guess_progress = ['_' for _ in word_to_guess]


def get_player_guess():
    """
    Prompts the player to enter their guess and validates it.

    :return: The player's validated guess as a lowercase alphabet character.
    """
    player_guess = input('Enter your guess: ').lower()
    while (not player_guess.isalpha() or len(player_guess) > 1 or
           player_guess in letters_guessed):

        if not player_guess.isalpha() or len(player_guess) > 1:
            print("Invalid input. Please enter a single alphabetic character.")
        if player_guess in letters_guessed:
            print(f"You already guessed {player_guess}")
        player_guess = input('Enter your guess: ').lower()

    return player_guess


def update_player_guess(guess, word_to_guess, player_guess_progress):
    """
    Updates the player's guess progress by replacing occurrences of the
    guessed character in the word to guess.

    :param guess: The character guessed by the player.
    :param word_to_guess: The word to guess.
    :param player_guess_progress: The current progress of the player's guesses.
    :return: The updated player's guess progress.
    """
    indices = [i for i, char in enumerate(word_to_guess) if char == guess]
    for index in indices:
        player_guess_progress[index] = guess
    return player_guess_progress


# game loop
while tries < MAX_TRIES:
    hangman_graphics.show_hangman(tries)
    if letters_guessed:
        print(f'You have guessed {letters_guessed}')
    print(' '.join(player_guess_progress))
    guess = get_player_guess()

    if guess in word_to_guess:
        player_guess_progress = update_player_guess(guess, word_to_guess,
                                                    player_guess_progress)



    elif guess not in word_to_guess:
        tries += 1

    letters_guessed.append(guess)

    if '_' not in player_guess_progress:
        print('The word was ' + ' '.join(word_to_guess))
        print(WINNER_MESSAGE)
        break

# Game Over
if tries == MAX_TRIES:
    hangman_graphics.show_hangman(tries)
    print('The word was ' + ' '.join(word_to_guess))
    print(LOSER_MESSAGE)
