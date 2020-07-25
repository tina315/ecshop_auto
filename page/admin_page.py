'''后台管理员登录页面类'''
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class AdminPage(BasePage):
    '''后台管理员登录页面类'''

    #定位器
    locator_admin_name = (By.NAME,'username')
    locator_admin_password = (By.NAME,'password')
    locator_submit = (By.CLASS_NAME,'button')

    def ele_admin_name(self,name):
        '''输入管理员用户名'''
        self.driver.find_element(*self.locator_admin_name).clear()
        self.driver.find_element(*self.locator_admin_name).send_keys(name)

    def ele_admin_password(self,password):
        '''输入管理员密码'''
        self.driver.find_element(*self.locator_admin_password).clear()
        self.driver.find_element(*self.locator_admin_password).send_keys(password)

    def ele_submit(self):
        '''提交登录'''
        self.driver.find_element(*self.locator_submit).click()

    def admin_login(self,name,password):
        '''后台管理员登录'''
        self.open_back_page()
        self.ele_admin_name(name)
        self.ele_admin_password(password)
        self.ele_submit()
        result = self.driver.current_url
        return result
