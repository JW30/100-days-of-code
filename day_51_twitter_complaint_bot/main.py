from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import keys
from time import sleep

PROMISED_DOWN: int = 500
PROMISED_UP: int = 200

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(f"{keys.CHROME_DRIVER_PATH}", options=chrome_options)
driver.get(url="https://www.speedtest.net/")
driver.maximize_window()

# Accept cookies
sleep(2)
try:
    driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]').click()
except NoSuchElementException:
    pass
else:
    sleep(2)

# Click on the Go button
driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()

# Wait until finished
WebDriverWait(driver, 120).until(ec.element_to_be_clickable(driver.find_element(by=By.CLASS_NAME, value="result-label")))

# Get download and upload speed
down = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
up = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

# Check if down or up is slower than promised by provider
if float(down) < PROMISED_DOWN or float(up) < PROMISED_UP:

    driver.get(url="https://twitter.com/")

    # Accept cookies
    sleep(2)
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div').click()
    except NoSuchElementException:
        pass
    else:
        sleep(2)

    # Click sign in
    driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div').click()

    # Enter Email and click next
    sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(keys.MY_GMAIL)
    driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()

    # Enter username if needed
    sleep(2)
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(keys.TWITTER_USERNAME)
        driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
    except:
        pass
    else:
        sleep(2)

    # Enter password and click Log in
    driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(keys.TWITTER_PW)
    driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()

    # Create message
    message: str = f"Hey Internet Provider, why is my internet speed {down}down/{up}up " \
                   f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

    # Click large Tweet button
    sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()

    # Enter message and click Tweet
    sleep(2)
    input_field = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    input_field.click()
    input_field.send_keys(message)
    driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]').click()
