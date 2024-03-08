from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Job Bank homepage
driver.get("https://www.jobbank.gc.ca/home")
time.sleep(2)

# Perform cursor move to the menu
dropdown_menu = driver.find_element("xpath", "/html/body/header/nav/div/div/ul/li[2]/a")
action = ActionChains(driver)
action.move_to_element(dropdown_menu).perform()
time.sleep(2)

# Click the School to Work link
child_menu = driver.find_element("xpath","/html/body/header/nav/div/div/ul/li[2]/ul/li[2]/a")
child_menu.click()
time.sleep(3)

# Click the Quizzes button
career_quizzes = driver.find_element("id","quizzes-link")
career_quizzes.click()
time.sleep(3)

# Click the first quiz button
take_the_quiz = driver.find_element("id","quizzHomeForm:j_id_2m_1_1c")
take_the_quiz.click()
time.sleep(3)

# Declare a quizzes counter to calculate
quizzes_counter = 0

while quizzes_counter < 50:
    # Dynamic concat element id to iterate
    radio_button = driver.find_element("id", f"workperferenceQuiz:Q-{quizzes_counter}:1")
    radio_button.click()
    # Click the next button when the current page is filled
    if quizzes_counter % 10 == 9:
        next_button = driver.find_element("id", "get-next")
        next_button.click()
        time.sleep(3)
    quizzes_counter += 1

time.sleep(5)
# Closing the webdriver
driver.close()
