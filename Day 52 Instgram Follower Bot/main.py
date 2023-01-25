from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import time

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
target_account = "mosesmoody"


class InstaFollower:

    def __init__(self):
        chrome_driver_path = "D:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(f"https://www.instagram.com/")
        self.ignored_exceptions = (
            NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException)
        self.wait = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions)
        self.driver.maximize_window()

    def login(self):
        username_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        username = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, username_xpath)))
        username.send_keys(INSTAGRAM_USERNAME)

        password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        password = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, password_xpath)))
        password.send_keys(INSTAGRAM_PASSWORD)

        log_in_xpath = '//*[@id="loginForm"]/div/div[3]/button'
        log_in = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, log_in_xpath)))
        log_in.click()

        skip_popups_xpath = '//*[@id="react-root"]/section/main/div/div/div/div/button'
        skip_popups = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, skip_popups_xpath)))
        skip_popups.click()

        # get current window
        # base_window = self.driver.current_window_handle
        # # Check for number of windows open
        # assert len(self.driver.window_handles) == 1
        # # # wait until number of window is 2
        # WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        # popup_window = self.driver.window_handles[1]
        # self.driver.switch_to.window(popup_window)
        # print(self.driver.title)

        notifications_off_xpath = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/' \
                                  'div/div[2]/div/div/div[3]/button[2]'
        notify = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, notifications_off_xpath)))
        notify.click()

        # self.driver.switch_to.window(base_window)

    def find_followers(self):
        search_xpath = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]' \
                       '/div/div/div[2]/input'
        search = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, search_xpath)))
        # search.click()
        search.send_keys(target_account)
        # search.send_keys(Keys.ENTER)
        search_results_xpath = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]' \
                               '/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a'
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, search_results_xpath))).click()

        followers_xpath = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/' \
                          'div/header/section/ul/li[2]/a/div'
        followers_link = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, followers_xpath)))
        followers_link.click()

    def follow(self):
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/'
                                                   'div/div[2]/div/div/div/div/div[2]/div')
        count = 2
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element
            # by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            try:
                follow_xpath = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]' \
                               f'/div/div/div[2]/div[1]/div/div[{count}]/div[3]/button'
                follow = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, follow_xpath)))
                follow.click()
            except ElementClickInterceptedException:
                cancel_xpath = '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]' \
                                   '/div/div/div/div/div[2]/div/div/div[3]/button[2]'
                cancel = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, cancel_xpath)))
                cancel.click()

            count += 1
            print(count)
            print("rolled")
            time.sleep(2)


insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()

# scroll_pause_time = 0.5
#
# # Get scroll height
# last_height = self.driver.execute_script("return document.body.scrollHeight")
#
# while True:
#     # Scroll down to bottom
#     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Wait to load page
#     time.sleep(scroll_pause_time)
#     try:
#         follow = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, follow_xpath)))
#         follow.click()
#     except ElementClickInterceptedException:
#         cancel_xpath = '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]' \
#                        '/div/div/div/div/div[2]/div/div/div[3]/button[2]'
#         cancel = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, cancel_xpath)))
#         cancel.click()
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = self.driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
