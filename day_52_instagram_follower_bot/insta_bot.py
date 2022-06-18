import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options
from time import sleep
import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

HASHTAG: str = "#mountains"


class InstaBot(webdriver.Chrome):

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        super().__init__(executable_path=keys.CHROME_DRIVER_PATH, options=chrome_options)

    def log_in(self):
        self.get(url="https://www.instagram.com/")
        self.maximize_window()

        # Accept cookies
        sleep(2)
        self.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/button[2]').click()

        # Enter email and pw and click log in
        sleep(2)
        email_input = self.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.send_keys(keys.INSTA_USER)
        pw_input = self.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        pw_input.send_keys(keys.INSTA_PW)
        sleep(2)
        self.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()

    def search_for_hashtag(self, hashtag: str):
        # Enter hashtag to search bar
        sleep(2)
        search_bar = WebDriverWait(self, 10).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
        search_bar.send_keys(hashtag)
        sleep(2)

        # Click on 1st suggestion
        WebDriverWait(self, 10).until(ec.visibility_of_element_located(
            (By.XPATH,
             '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div'))).click()
        self.implicitly_wait(20)

    def like_and_follow_image(self, xpath):
        # Open image, like and follow the creator
        sleep(2)
        img = self.find_element(by=By.XPATH, value=xpath)
        WebDriverWait(self, 10).until(ec.element_to_be_clickable(img)).click()
        sleep(3)
        try:
            follow_btn = self.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/div/div'
                                                              '/div[1]/div/div[3]/div/div/div/div/div[2]/div'
                                                              '/article/div/div[2]/div/div/div[1]/div/header'
                                                              '/div[2]/div[1]/div[2]/button')
            if follow_btn.text != "Following":
                follow_btn.click()
                # Click like
                self.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
                                                     '/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]'
                                                     '/div/div/div[2]/section[1]/span[1]/button').click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        # Click X
        self.find_element(
            by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div').click()

    def like_and_follow_images(self, amount: int):
        for x in range(amount):
            current_xpath: str = f"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]" \
                                 f"/div[1]/section/main/article/div[2]/div/div[{(x // 3) + 1}]/div[{(x % 3) + 1}]/a"
            self.like_and_follow_image(xpath=current_xpath)


bot = InstaBot()
bot.log_in()
bot.search_for_hashtag(hashtag=HASHTAG)
bot.like_and_follow_images(amount=100)
