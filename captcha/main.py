import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from solveRecaptcha import SolveRecaptcha

drivers_directory = r"D:"
os.environ['PATH'] += os.pathsep + drivers_directory
options = Options()
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)
driver.get("https://google.com/recaptcha/api2/demo")

result = SolveRecaptcha(
    "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
    "https://www.google.com/recaptcha/api2/demo"
)

code = result['code']

print(code)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
)

driver.execute_script(
    "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")

driver.find_element(By.ID, "recaptcha-demo-submit").click()

time.sleep(120)