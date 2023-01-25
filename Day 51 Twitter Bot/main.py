from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import os
import time

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
UPLOAD_SPEED = 20
DOWNLOAD_SPEED = 500


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_driver_path = "D:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get("https://www.speedtest.net/")
        self.ignored_exceptions = (
            NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException)
        self.up_speed = 0
        self.down_speed = 0

    """Speed Test side of things"""

    def get_internet_speed(self):
        go_button_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        go_button = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, go_button_xpath)))
        go_button.click()

        time.sleep(45)
        up_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]' \
                   '/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        up_speed = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, up_xpath)))
        self.up_speed = up_speed.get_attribute("innerHTML")
        print(self.up_speed)

        down_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]' \
                     '/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
        down_speed = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, down_xpath)))
        self.down_speed = down_speed.text
        print(self.down_speed)

    """Twitter side of Things"""

    def tweet_at_provider(self):
        chrome_driver_path = "D:\Development\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        driver.get("https://twitter.com/i/flow/signup")
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException)

        # sign in button
        sign_in_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]' \
                        '/div/div/div/div[7]/span[2]'
        sign_in = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, sign_in_xpath)))
        sign_in.click()

        # email entry
        email_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/' \
                      'div/div/div/div[5]/label/div/div[2]/div/input'
        email = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, email_xpath)))
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        # phone_number entry
        phone_input_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]' \
                            '/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
        phone_input = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, phone_input_xpath)))
        phone_input.send_keys(PHONE_NUMBER)
        phone_input.send_keys(Keys.ENTER)

        # password entry
        password_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]' \
                         '/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        password = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, password_xpath)))
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        # tweet
        tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
        tweet = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, tweet_xpath)))
        tweet.click()

        # Type Tweet
        typing_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]' \
                       '/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]' \
                       '/div/div/div/div/div/div[2]/div'
        input_tweet = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, typing_xpath)))
        input_tweet.click()
        input_tweet.send_keys(
            f"Hey @Rogers, why is my internet speed {self.down_speed}down/ {self.up_speed}up when I pay for"
            f" {DOWNLOAD_SPEED}down/{UPLOAD_SPEED}up? #Pythonbot #Selenium #TestingmyCode ")

        tweet_xpath = ('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div'
                       '/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_button = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, tweet_xpath)))
        tweet_button.click()
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

"""Notes """

# get current window
# base_window = driver.current_window_handle
# # Check for number of windows open
# assert len(driver.window_handles) == 1
# # check internet speed
# # speed_test = InternetSpeedTwitterBot()
# # speed_test.get_internet_speed()
# # wait until number of window is 2
# WebDriverWait(driver, 60).until(expected_conditions.number_of_windows_to_be(2))
#
# # loop through until we find a new window handle
# for window_handle in driver.window_handles:
#     if window_handle != base_window:
#         driver.switch_to.window(window_handle)
#         break

# WebDriverWait(driver, 10,).until(expected_conditions.title_is("Speedtest by Ookla "))
