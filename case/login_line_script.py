'''
case:login
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# open chrome
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
# open ecshop front page
url = "http://192.168.1.40/upload/user.php"
driver.get(url=url)
print(driver.current_url)
# login
driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys("wanghh")
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys("123456")
driver.find_element(By.NAME,'submit').click()
time.sleep(2)
# close and quit
driver.quit()