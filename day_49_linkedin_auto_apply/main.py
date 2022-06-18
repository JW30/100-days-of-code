from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import keys

driver = webdriver.Chrome(f"{keys.CHROME_DRIVER_PATH}")
driver.get(url="https://www.linkedin.com/jobs/search/?f_AL=true&geoId=103644278&keywords=python&location=United%20States")

driver.implicitly_wait(time_to_wait=10)
# Accept cookies and click sign in
driver.find_element(by=By.XPATH, value="//*[@id='artdeco-global-alert-container']/div/section/div/div[2]/button[1]").click()
driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]").click()

driver.implicitly_wait(time_to_wait=10)
# Enter Email and PW and click sign in
driver.find_element(by=By.NAME, value="session_key").send_keys(keys.LINKEDIN_EMAIL)
driver.find_element(by=By.NAME, value="session_password").send_keys(keys.LINKEDIN_PW)
driver.find_element(by=By.XPATH, value="//*[@id='organic-div']/form/div[3]/button").click()

driver.implicitly_wait(time_to_wait=10)
job_list = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-search-results")
job_results = job_list.find_elements(By.CSS_SELECTOR, value=".jobs-search-results__list-item")

for job in job_results:
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable(job))
    while True:
        try:
            job.find_element(by=By.CSS_SELECTOR, value=".job-card-list__title").click()
        except ElementClickInterceptedException:
            # Close Pop-Up
            driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-toast-item__dismiss").click()
        else:
            save_btn = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
            WebDriverWait(driver, 20).until(ec.element_to_be_clickable(save_btn))
            save_btn.click()
            break

driver.quit()



