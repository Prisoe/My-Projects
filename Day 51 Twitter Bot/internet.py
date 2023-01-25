from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys



# class InternetSpeedTwitterBot:
#
#
#     def __init__(self):
#         chrome_driver_path = "D:\Development\chromedriver.exe"
#         self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
#         self.driver.get("https://www.speedtest.net/")
#         self.ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException)
#         self.up_speed = 0
#         self.down_speed = 0
#
#
#     def get_internet_speed(self):
#         go_button_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
#         go_button = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions)\
#                         .until(expected_conditions.presence_of_element_located((By.XPATH, go_button_xpath)))
#         go_button.click()
#
#         # result_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a'
#         # results = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions)\
#         #                 .until(expected_conditions.presence_of_element_located((By.XPATH, result_xpath)))
#         # results.click()
#
#         up_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
#         up_speed = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions)\
#                         .until(expected_conditions.presence_of_element_located((By.XPATH, up_xpath)))
#         self.up_speed = up_speed.text
#
#         down_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
#         down_speed = WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions)\
#                         .until(expected_conditions.presence_of_element_located((By.XPATH, down_xpath)))
#         self.down_speed = down_speed.text
#
#         print(self.up_speed, self.down_speed)
#
#
#     def tweet_at_provider(self):
#         pass