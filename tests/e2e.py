# import webdriver from selenium package
from selenium import webdriver

import Utils


def test_scores_service(app_url):
    result = True
    # open chrome via webdriver
    driver = webdriver.Chrome(executable_path=".\\chromedriver.exe")
    # wait a bit for browser to be ready
    driver.implicitly_wait(10)

    # navigate to score site
    driver.get(app_url)

    # look for score element in DOM
    score = driver.find_element_by_id("score")

    # validate the score value
    result = validate_score(score.text)
    print(score.text)
    print(result)
    return result


# score validation function. Return True for valid value and false otherwise
def validate_score(score):
    int_score = int(score)
    print(int_score)
    return Utils.SCORE_MAX > int_score > Utils.SCORE_MIN


# main function invoke test function. Return 0 in case of success, -1 otherwise
def main_function():
    test_result = -1
    if test_scores_service(Utils.get_app_url()):
        test_result = 0

    return test_result


if __name__ == "__main__":
    main_function()
