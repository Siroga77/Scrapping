from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Programming\Python\Selenium\chromedriver.exe")

link = 'https://www.google.com'

try:
    driver.get(link)
    search = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]')
    search.send_keys("lol")
    time.sleep(1)
    sendRequest = driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
    sendRequest.click()


finally:
    driver.quit()



