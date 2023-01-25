from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import time

PHONE = os.getenv("PHONE")
PASSWORD = os.getenv("PASSWORD")

chrome_driver_path = "D:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException)

log_in_tinder_xpath = '//*[@id="t-188693591"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
log_in_tinder_link = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, log_in_tinder_xpath)))
log_in_tinder_link.click()


allow_cookies_xpath = '//*[@id="t-188693591"]/div/div[2]/div/div/div[1]/div[1]/button'
allow_cookies = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, allow_cookies_xpath)))
allow_cookies.click()

log_in_xpath = '//*[@id="t-1917074667"]/main/div/div[1]/div/div/div[3]/span/div[2]/button'
log_in_facebook = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, log_in_xpath)))
log_in_facebook.click()


# Switch windows

base_window = driver.window_handles[0]
print(driver.title)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

phone_number_xpath = '//*[@id="email"]'
phone_number = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, phone_number_xpath)))
phone_number.send_keys("6475754993")


password_xpath = '//*[@id="pass"]'
password = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, password_xpath)))
password.send_keys("Probol@26")


log_in_xpath = '//*[@id="loginbutton"]'
log_in = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, log_in_xpath)))
log_in.click()

driver.switch_to.window(base_window)
# tinder_phone_number_xpath = '//*[@id="u916312630"]/div/div/div[1]/div/div[2]/div/input'
# tinder_phone_number = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
#                         .until(expected_conditions.presence_of_element_located((By.XPATH, tinder_phone_number_xpath)))
# tinder_phone_number.send_keys("6475754993")


# continue_button_xpath = '//*[@id="u916312630"]/div/div/div[1]/div/button'
# continue_button = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
#                         .until(expected_conditions.presence_of_element_located((By.XPATH, continue_button_xpath)))
# continue_button.click()


# Switch windows
# base_window = driver.window_handles[0]
# fb_login_window = driver.window_handles[1]
# driver.switch_to.window(base_window)
# print(driver.title)

driver.switch_to.window(base_window)
time.sleep(10)

#Allow location
allow_location_xpath = '//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[1]'
allow_location_button = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, allow_location_xpath)))
allow_location_button.click()


#Disallow notifications
notifications_xpath = '//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[2]'
notifications_button = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, notifications_xpath)))
notifications_button.click()

# #Allow cookies
# cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
# cookies.click()

# remind me later button
# remind_xpath = '//*[@id="t-1917074667"]/main/div/div[1]/div/div[2]/button[2]'
# remind_button = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
#                         .until(expected_conditions.presence_of_element_located((By.XPATH, remind_xpath)))
# remind_button.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(5)

    try:
        print("called")
        like_button_xpath ='//*[@id="t-188693591"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button'
        like_button = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH, like_button_xpath)))
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()