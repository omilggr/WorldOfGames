# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty.
import random
import Utils


# generate random number between 1 and the user difficulty selection and return it to the calling function
def generate_number(difficulty):
    generated_number = random.randint(1, difficulty)
    return generated_number


# get the user's guess and return it to the calling function
def get_guess_from_user(difficulty):
    success = False
    while not success:
        try:
            user_number = int(input('Please enter a number between 1 and %s: ' % difficulty))
            success = 1 <= user_number <= difficulty

            if not success:
                print(Utils.WRONG_SELECTION_MESSAGE)

        except ValueError:
            print(Utils.ERROR_MESSAGE)

        return user_number


# compare between random generated number and user's input. Returning true in case of match, false otherwise
def compare_results(difficulty, secret_number):
    return get_guess_from_user(difficulty) == secret_number


# guess game execution function. Generate random number by using generate_number function,
# invoke compare_results function and return game result to the calling function
def play(difficulty):
    generated_number = generate_number(difficulty)
    return compare_results(difficulty, generated_number)
