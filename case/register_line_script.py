'''
case:register
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
# open chrome
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
# open ecshop front page
url = "http://192.168.1.40/upload/user.php?act=register"
driver.get(url=url)
print(driver.current_url)
# register
# '''输入用户名'''
driver.find_element(By.ID,'username').clear()
driver.find_element(By.ID,'username').send_keys('wangll')
# '''输入邮箱'''
driver.find_element(By.ID, 'email').clear()
driver.find_element(By.ID, 'email').send_keys('159@qq.com')
# '''输入密码'''
driver.find_element(By.ID, 'password1').clear()
driver.find_element(By.ID, 'password1').send_keys('123456')
# '''输入确认密码'''
driver.find_element(By.ID, 'conform_password').clear()
driver.find_element(By.ID, 'conform_password').send_keys('123456')
# '''提交注册'''
driver.find_element(By.NAME, 'Submit').click()
#close and quit
driver.quit()