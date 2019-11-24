# contains a general operations and parameters for the system
import os

ERROR_MESSAGE = 'Something went wrong\n'
WRONG_SELECTION_MESSAGE = 'Wrong selection\n'

SCORE_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = "ERROR"

WINNING_MESSAGE = "You won"
LOSS_MESSAGE = "You lose"


# this function clears the screen
def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


