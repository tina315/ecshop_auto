'''
case:shopping in ecshop front page
'''

#import webdriver
from  selenium import  webdriver
from selenium.webdriver.common.by import By
import time

#open chrome
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

#open ecshop front page
driver.get("http://localhost/upload/index.php")
time.sleep(2)

#login
#//*[@id="ECS_MEMBERZONE"]/a[1]
driver.find_element(By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]').click()
time.sleep(2)
driver.find_element_by_name('username').send_keys("bu知道11")
driver.find_element_by_name('password').send_keys("123456")
driver.find_element_by_name('submit').click()
time.sleep(3)

#search sweater
driver.find_element_by_id("keyword").send_keys("毛衣")
driver.find_element_by_name('imageField').click()
time.sleep(2)

#get in the second product
#//*[@id="compareForm"]/div/div[2]/a/img
driver.find_element(By.XPATH,'//form[@id="compareForm"]/div/div[2]/a/img').click()
time.sleep(2)

#join the product in shopcar
#//*[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img
driver.find_element(By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img').click()
time.sleep(2)

#go to by the product
#/html/body/div[7]/div[1]/table/tbody/tr/td[2]/a/img
driver.find_element(By.CSS_SELECTOR,'form[id="formCart"]+table>tbody>tr td:nth-child(2)>a>img').click()
time.sleep(2)

#submit order
#//*[@id="theForm"]/div[11]/div[2]/input[1]
driver.find_element(By.XPATH,'//form[@id="theForm"]/div[11]/div[2]/input[1]').click()
time.sleep(2)

#close and quit
driver.quit()