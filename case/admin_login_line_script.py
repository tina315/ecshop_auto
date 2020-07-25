'''
case:admin login
'''

#import webdriver
from  selenium import  webdriver
from selenium.webdriver.common.by import By
import time

#open chrome
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

#open ecshop back page
driver.get("http://localhost/upload/admin")
time.sleep(2)

#login
driver.find_element(By.NAME,'username').send_keys("admin")
driver.find_element(By.NAME,'password').send_keys("wd19960315")
driver.find_element(By.CLASS_NAME,'button').click()
time.sleep(3)

#close and quit
driver.quit()