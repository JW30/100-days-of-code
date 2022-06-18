from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import keys
from time import sleep

# If you enter your Chrome profile path, there will be no need to sign in again etc.
CHROME_PROFILE_PATH = None

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
if CHROME_PROFILE_PATH:
    chrome_options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
driver = webdriver.Chrome(f"{keys.CHROME_DRIVER_PATH}", options=chrome_options)
driver.get(url="https://tinder.com/")

if not CHROME_PROFILE_PATH:

    # Wait for page to load
    driver.implicitly_wait(time_to_wait=20)

    # Accept cookies
    driver.find_element(by=By.XPATH, value='//*[@id="o-654199900"]/div/div[2]/div/div/div[1]/div[1]/button').click()

    # Click login button
    driver.find_element(by=By.LINK_TEXT, value="Log in").click()

    # Click log in with phone number
    sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="o1912386320"]/div/div/div[1]/div/div/div[3]/span/div[3]/button').click()

    # Enter phone number and click continue
    sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="o1912386320"]/div/div/div[1]/div/div[2]/div/input').send_keys(keys.PHONE_NUMBER)
    driver.find_element(by=By.XPATH, value='//*[@id="o1912386320"]/div/div/div[1]/div/button').click()

    # Allow to manually enter 2-factor-code
    sleep(20)

    # Click continue button
    driver.find_element(by=By.XPATH, value='//*[@id="o1912386320"]/div/div/div[1]/div/button').click()

    # Allow to manually enter Email code
    sleep(20)

    # Click confirm Email
    driver.find_element(by=By.XPATH, value='//*[@id="o1912386320"]/div/div/div[1]/div/button').click()

    # Allow to share location
    sleep(2)
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="o1912386320"]/div/div/div/div/div[3]/button[1]').click()
    except NoSuchElementException:
        pass
    else:
        sleep(2)

    # Don't allow notifications
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="o1912386320"]/div/div/div/div/div[3]/button[1]').click()
    except NoSuchElementException:
        pass

# Swipe right 20 times
for _ in range(20):
    sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
