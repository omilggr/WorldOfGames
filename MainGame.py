# start World of the game
from Live import load_game, welcome

# get user's name and print welcome message by using welcome function
name = str(input('Insert your name, please: '))
welcome(name)

# load and execute the game according to user selection
load_game()

