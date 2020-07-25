'''登录页面类'''
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class LoginPage(BasePage):
    '''登录页面类'''
    #定位器
    locator_open_login_page = (By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]')
    locator_username = (By.NAME, 'username')
    locator_password = (By.NAME, 'password')
    locator_submit = (By.NAME, 'submit')
    locator_assert = locator_open_login_page

    def open_login_page(self):
        '''打开登录页面'''
        self.driver.find_element(*self.locator_open_login_page).click()

    def ele_username(self,username):
        '''输入用户名'''
        self.driver.find_element(*self.locator_username).clear()
        self.driver.find_element(*self.locator_username).send_keys(username)

    def ele_password(self,password):
        #密码定位操作
        self.driver.find_element(*self.locator_password).clear()
        self.driver.find_element(*self.locator_password).send_keys(password)

    def ele_submit(self):
        #登录按钮定位操作
        self.driver.find_element(*self.locator_submit).click()

    def login(self,username,password):
        self.open_front_page()
        self.open_login_page()
        self.ele_username(username)
        self.ele_password(password)
        self.ele_submit()
        result = self.assert_result(self.locator_assert)
        return result