'''基础页面类'''
from selenium.webdriver.common.by import By
from data.base_data import front_url, back_url


class BasePage():
    '''基础页面类'''

    #定位器
    locator_product_management = (By.XPATH, '//ul[@id="menu-ul"]/li[1]')

    def __init__(self,driver):
        '''初始化'''
        self.driver = driver

    def open_front_page(self):
        '''打开前台页面'''
        self.driver.get(url=front_url)

    def open_back_page(self):
        '''打开前台页面'''
        self.driver.get(url=back_url)

    def assert_result(self,loc):
        '''断言'''
        result = self.driver.find_element(*loc).text
        return result

    def switch_to_frame(self,frame):
        '''切入内联框架'''
        self.driver.switch_to.frame(frame)

    def switch_to_parent_frame(self):
        '''切入父内联框架'''
        self.driver.switch_to.parent_frame()

    def switch_out_frame(self):
        '''切出内联框架'''
        self.driver.switch_to.default_content()

    def product_management(self):
        '''点击商品管理'''
        self.driver.find_element(*self.locator_product_management).click()
