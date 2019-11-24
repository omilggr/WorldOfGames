# the purpose of memory game is to display an amount of random numbers to the users for 0.7 seconds
# and then prompt the user for the numbers that he remember. User wins if he remembers all the numbers;
# he loses otherwise.

import random
import Utils
import time

MIN_NUMBER = 1
MAX_NUMBER = 101


# this function generates a list of random numbers between MIN_NUMBER and MAX_NUMBER.
# the list length is difficulty (selected by the user)
# the generated list is returned to the calling function
def generate_sequence(difficulty):
    generated_list = []
    for index in range(difficulty):
        generated_list.append(random.randint(MIN_NUMBER, MAX_NUMBER))

    return generated_list


# this function prompt the user for the list he remember and returns it to the calling function
def get_list_from_user(difficulty):
    user_list = []

    print('After seeing the numbers enter the numbers you saw, each one separated with Enter.')
    
    for index in range(difficulty):
        success = False
        while not success:
            try:
                user_input = int(input())
                user_list.append(user_input)

                success = True
            except ValueError:
                print('Please enter an integer value')

    return user_list


# this function compares the generated list with the list inserted by the user
def is_list_equal(list_a, list_b):
    result = True;
    for index in range(len(list_a)):
        result &= list_a[index] == list_b[index]

    return result


# memory game execution function. Generate a list of a random numbers by using generate_sequence function,
# print the list on the std out, clean the screen after 0.7 seconds and 
# invoke compare_results function and return game result to the calling function
def play(difficulty):
    generated_list = generate_sequence(difficulty)
    for index in range(len(generated_list)):
        print(generated_list[index])

    # after printing the generated list wait 0.7 sec
    time.sleep(0.7)
    # clean the screen
    Utils.screen_cleaner()
    # prompt the user for the list and compare the result. return the comparison result to the calling function
    return is_list_equal(generated_list, get_list_from_user(difficulty))
