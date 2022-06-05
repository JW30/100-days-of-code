from time import time_ns
from selenium import webdriver
from selenium.webdriver.common.by import By
import keys


class CookieClicker:

    def __init__(self):
        self.driver = webdriver.Chrome(f"{keys.CHROME_DRIVER_PATH}")
        self.driver.get(url="https://orteil.dashnet.org/cookieclicker/")
        self.driver.find_element(by=By.ID, value="langSelect-DE").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/a[1]").click()
        self.cookie = self.driver.find_element(by=By.ID, value="bigCookie")
        self.products = {}
        self.cookies = 0

    def run(self):
        last_time_checked = time_ns()
        while True:
            time = time_ns()
            if time - last_time_checked > 5e9:
                self.update_cookies()
                self.buy_product()
                last_time_checked = time
            self.cookie.click()

    def buy_product(self):
        products = self.driver.find_elements(by=By.CSS_SELECTOR, value="#products .unlocked")
        most_expensive_index = -1
        most_expensive_price = -1
        for i, p in enumerate(products):
            price = int(p.find_element(by=By.CLASS_NAME, value="price").text.replace(",", ""))
            if most_expensive_price < price <= self.cookies:
                most_expensive_index = i
        if most_expensive_index > -1:
            product = products[most_expensive_index]
            owned = product.find_element(by=By.CLASS_NAME, value="owned").text
            if not owned or int(owned) < 15:
                product.click()

    def update_cookies(self):
        cookies_text = self.driver.find_element(by=By.ID, value="cookies").text
        self.cookies = int(cookies_text.split()[0].replace(",", ""))


cc = CookieClicker()
cc.run()
