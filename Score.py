# this file manages the scores files
import Utils
import os.path


# add_score function calculate and store a user score
def add_score(points):
    try:
        score = 0
        # if score file exist, open it for read and get the current score from it.
        if os.path.exists(Utils.SCORE_FILE_NAME):
            score_file = open(Utils.SCORE_FILE_NAME, mode="r+")
            line = score_file.read()
            score = int(line)
            score_file.close()

        # open scores files for updating a new score. create the file if it doesn't exist
        score_file = open(Utils.SCORE_FILE_NAME, mode="w+")
        print('your prev score is %s points' % score)
        score += int(points)
        print('your new  score is %s points' % score)
        # save the new score to the file
        score_file.write(str(score))
        score_file.close()
    except IOError:
        print(Utils.ERROR_MESSAGE)


