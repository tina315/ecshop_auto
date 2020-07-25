'''注册页面类'''
from page.base_page import BasePage
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    '''注册页面类'''

    #定位器
    locator_open_register_page = (By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[2]')
    locator_username = (By.ID,'username')
    locator_email = (By.ID, 'email')
    locator_password = (By.ID, 'password1')
    locator_confirm_password = (By.ID, 'conform_password')
    locator_submit = (By.NAME, 'Submit')
    locator_assert = (By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]')


    def open_register_page(self):
        '''打开前台页面'''
        self.driver.find_element(*self.locator_open_register_page).click()

    def ele_username(self,username):
        '''输入用户名'''
        self.driver.find_element(*self.locator_username).clear()
        self.driver.find_element(*self.locator_username).send_keys(username)

    def ele_email(self,email):
        '''输入邮箱'''
        self.driver.find_element(*self.locator_email).clear()
        self.driver.find_element(*self.locator_email).send_keys(email)

    def ele_password(self,password):
        '''输入密码'''
        self.driver.find_element(*self.locator_password).clear()
        self.driver.find_element(*self.locator_password).send_keys(password)

    def ele_confirm_password(self,confirm_password):
        '''输入确认密码'''
        self.driver.find_element(*self.locator_confirm_password).clear()
        self.driver.find_element(*self.locator_confirm_password).send_keys(confirm_password)

    def ele_submit_register(self):
        '''提交注册'''
        self.driver.find_element(*self.locator_submit).click()

    def register(self,username,email,password,confirm_password):
        '''注册流程'''
        self.open_front_page()
        self.open_register_page()
        self.ele_username(username)
        self.ele_email(email)
        self.ele_password(password)
        self.ele_confirm_password(confirm_password)
        self.ele_submit_register()
        result = self.assert_result(self.locator_assert)
        return result
