'''初始化浏览器驱动'''
from selenium import webdriver


def chrome_driver():
    '''初始化浏览器驱动'''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver