
def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """

    return("GOT TO EASY")
    # TODO
    pass


def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    # TODO
    return("GOT TO MED")
    pass


def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    # TODO
    return("GOT TO HARD")
    pass


def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    # TODO
    pass


def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    # TODO
    pass


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    # TODO
    pass


def main():
    """
    Runs when the program is called from the command-line.

            1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """
    # TODO
    # print("Welcome to Mystery Word!")
    # while True:
    #     diff_choice = input("Please choose a difficulty level: Easy, Medium, or Hard\n>>>").lower()
    #     if diff_choice in ('easy', 'e', 'medium', 'med', 'm', 'hard', 'h'):
    #         break
    #     else:
    #         print("Not a valid input")

    with open ('/usr/share/dict/words') as f:
        if diff_choice in ('e', 'easy'):
            print(easy_words(f.read().split()))
        elif diff_choice in ('h', 'hard'):
            print(hard_words(f.read().split()))
        else:
            print(medium_words(f.read().split()))





if __name__ == '__main__':
    main()
