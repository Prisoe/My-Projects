from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os
import time

email_keys = os.environ.get("EMAIL_KEYS")
password_keys = os.environ.get("PASSWORD_KEYS")
PHONE = os.getenv("PHONE")


chrome_driver_path = "D:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# Sign in link
sign_in_link = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_link.click()


# email
email = driver.find_element(By.NAME, "session_key")
email.send_keys(email_keys)


# password
password = driver.find_element(By.NAME, "session_password")
password.send_keys(password_keys)


# Log in
button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
button.click()


# # # Job link
# job_link = driver.find_element(By.CSS_SELECTOR, '.jobs-search-results-list ul li')
# job_link.click()
# print(job_link)
# time.sleep(2)
# #
# #
# # Easy Apply
# time.sleep(5)
# apply_link = driver.find_element(By.XPATH, '//*[@id="ember407"]')
# apply_link.click()
# #
# # # next_link = driver.find_element(By.XPATH, '//*[@id="ember418"]').click()
# #
# #


# Try to locate the apply button, if can't locate then skip the job.
try:
    apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
    apply_button.click()
    time.sleep(5)

    # If phone field is empty, then fill your phone number.
    phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
    if phone.text == "":
        phone.send_keys(PHONE)

    submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

    # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
    if submit_button.get_attribute("data-control-name") == "continue_unify":
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)
        discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()
        print("Complex application, skipped.")
        # continue

    else:
        submit_button.click()

    # Once application completed, close the pop-up window.
    time.sleep(2)
    close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
    close_button.click()

# If already applied to job or job is no longer accepting applications, then skip.
except NoSuchElementException:
    print("No application button, skipped.")
    # continue

time.sleep(5)
# driver.quit()