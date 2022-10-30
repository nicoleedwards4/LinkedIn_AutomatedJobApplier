from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import credentials
import time

LINKEDIN_USER = credentials.linkedin_username
LINKEDIN_PASSWORD = credentials.linkedin_password

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3333278316&distance=25&f_AL=true&geoId=104976816&keywords" \
      "=data%20engineer&location=Tacoma%2C%20Washington%2C%20United%20States&refresh=true&sortBy=R "

driver.get(URL)
time.sleep(3)

sign_in = driver.find_element("xpath", "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

time.sleep(3)

email = driver.find_element("id", "username")
email.send_keys(LINKEDIN_USER)

password = driver.find_element("id", "password")
password.send_keys(LINKEDIN_PASSWORD)

sign_in_button = driver.find_element("xpath", '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()

all_listings = driver.find_elements("css selector", ".jobs-search-results__list-item")

for listing in all_listings:
    listing.click()
    time.sleep(5)
    save_button = driver.find_element("xpath", '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div['
                                               '1]/div[1]/div[3]/div/button/span[1]')
    save_button.click()

driver.close()
