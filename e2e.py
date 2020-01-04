# import webdriver from selenium package
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import Utils


def test_scores_service(app_url):
    result = True

    try:
        # set chrome options to run headless
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        # open chrome via webdriver
        driver = webdriver.Chrome(options=chrome_options)
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
    except NoSuchElementException as ex:
        print(ex)
    except:
        print(Utils.ERROR_MESSAGE)



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
