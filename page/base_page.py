'''基础页面类'''
from data.base_data import front_url, back_url


class BasePage():
    '''基础页面类'''

    #定位器

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
