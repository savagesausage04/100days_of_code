from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "/Users/kylehan/Development/chromedriver"
options = webdriver.ChromeOptions()
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3160031175&f_AL=true&geoId=103575230&keywords=python%20developer&location=Irvine%2C%20California%2C%20United%20States")

sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()

time.sleep(1)

email_sign_in = driver.find_element(By.ID, "username")
email_sign_in.send_keys("kyleh1104@gmail.com")

time.sleep(1)

password_sign_in = driver.find_element(By.ID, "password")
password_sign_in.send_keys("Sangjun04!")

time.sleep(1)

sign_in_actually = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
sign_in_actually.click()

time.sleep(5)

driver.maximize_window()
job_listings = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")
for job in job_listings:
    job.click()
    time.sleep(3)
    print(f"Saved: {job.text}")
    save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    save_button.click()

time.sleep(5)
driver.quit()