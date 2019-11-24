from GuessGame import play as play_guess_game
from MemoryGame import play as play_memory_game
import Score
import Utils


# this function gets a name of the game user and print a welcome message on the screen
def welcome(name):
    print('Hello %s and welcome to the World of Games.\nHere you can find many cool games to play.' % name)


# define switcher dictionary for supported games
def play_selected_game(selection, difficulty):
    switcher = {
        1: play_memory_game,
        2: play_guess_game,
     }
    # Get the function from switcher dictionary
    func = switcher.get(selection)
    # Execute the function
    return func(difficulty)


# this function invoke the game according to user game and difficulty selection
def load_game():
    text = 'Please choose a game to play or press 0 to quit:\n'\
        '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n'\
        '2. Guess Game - guess a number and see if you chose like the computer\n'\
        '0. Quit\n'

    quit_request = False
    # loop while user doesn't ask to quit
    while not quit_request:
        # get game selection or quit request from a user
        success = False

        # loop while user doesn't insert a legal game number or ask to quit
        while not success and not quit_request:
            try:
                game_id = int(input(text))
                success = 1 <= game_id <= 2
                quit_request = game_id == 0

                if not success and not quit_request:
                    print(Utils.WRONG_SELECTION_MESSAGE)

            except ValueError:
                print(Utils.ERROR_MESSAGE)

        # if user's selected a game, get a difficulty level
        if not quit_request:
            success = False
            # loop while user doesn't insert a legal difficulty level or ask to quit
            while not success and not quit_request:
                try:
                    game_level = int(input('Please choose a game difficulty from 1 to 5 or 0 to quit: '))
                    success = 1 <= game_level <= 5
                    quit_request = game_level == 0
                    if not success and not quit_request:
                        print(Utils.WRONG_SELECTION_MESSAGE)

                except ValueError:
                    print(Utils.ERROR_MESSAGE)

            # if user's selected a game and the difficulty level - start game execution
            # add score to the user's current score in case of success
            if not quit_request:
                if play_selected_game(game_id, game_level):
                    print(Utils.WINNING_MESSAGE)
                    Score.add_score(game_level)
                else:
                    print(Utils.LOSS_MESSAGE)


