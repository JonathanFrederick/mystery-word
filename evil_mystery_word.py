import random

def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    easy_list = []
    for word in word_list:
        if len(word) < 7 and len(word) > 3:
            easy_list.append(word)
    return(easy_list)

def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    med_list = []
    for word in word_list:
        if len(word) < 9 and len(word) > 5:
            med_list.append(word)
    return(med_list)

def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    hard_list = []
    for word in word_list:
        if len(word) > 7:
            hard_list.append(word)
    return(hard_list)

def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    return random.choice(word_list)

def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    display = ''
    for letter in word:
        if letter in guesses:
            display += letter.upper()
        else:
            display += '_'
        if len(display) < len(word)*2-1:
            display += ' '
    return display

def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    for letter in word:
        if letter not in guesses:
            return False
    return True


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
    again = True
    while again:
        print("Welcome to Mystery Word!")
        while True:
            diff_choice = input("Please choose a difficulty level: Easy, Medium, or Hard\n>>> ").lower()
            if diff_choice in ('easy', 'e', 'medium', 'med', 'm', 'hard', 'h'):
                break
            else:
                print("Not a valid input")

        #open dictionary word list
        with open ('/usr/share/dict/words') as f:
            if diff_choice in ('e', 'easy'):
                mys_word_list = easy_words(f.read().split())
            elif diff_choice in ('h', 'hard'):
                mys_word_list = hard_words(f.read().split())
            else:
                mys_word_list = medium_words(f.read().split())

        mys_word = random_word(mys_word_list)
        guesses = []
        wrong = -1
        #turn loop
        while wrong < 8:
            #display word
            print("Your word is ", display_word(mys_word, guesses))
            if wrong > -1:
                print("You have guessed", end=" ")
                for j in guesses:
                    print(j, end = " ")
                print('')
            else:
                wrong += 1
            #get guesses
            while True:
                guess = input("Please choose a letter, you have " + str(8-wrong) + " of 8 wrong guesses left\n>>> ")
                if guess in guesses:
                    print("You have already guessed that letter")
                elif len(guess) == 1 and guess.isalpha():
                    guesses.append(guess)
                    break
                else:
                    print("Invalid input")
            #count wrong guesses

            if mys_word.find(guess) == -1:
                wrong += 1
            #check for win
            if (is_word_complete(mys_word, guesses)):
                print("Congratulations! You guessed the word! This word was", mys_word.upper())
                break

        #check for loss
        if not is_word_complete(mys_word, guesses):
            print("Sorry, you did not guess the word, it was", mys_word.upper())
        #ask to play again
        while True:
            again_choice = input("Would you like to play again? (Yes or No)").lower()
            if again_choice in ('yes', 'y', 'no', 'n'):
                break
            else:
                print("Not a valid input")
        if again_choice in ('no', 'n'):
            again = False

if __name__ == '__main__':
    main()
