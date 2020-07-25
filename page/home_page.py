'''前台首页类'''
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page.base_page import BasePage


class HomePage(BasePage):
    '''前台首页类'''

    #定位器
    locator_keyword = (By.ID,'keyword')
    locator_shopcar = (By.XPATH,'//li[@id="ECS_CARTINFO"]/a')
    locator_add_shopcar = (By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img')

    def get_in_shopcar(self):
        '''首页进入购物车'''
        self.driver.find_element(*self.locator_shopcar).click()

    def key_word(self,keyword):
        '''关键字搜索'''
        self.driver.find_element(*self.locator_keyword).clear()
        self.driver.find_element(*self.locator_keyword).send_keys(keyword)
        self.driver.find_element(*self.locator_keyword).send_keys(Keys.ENTER)

    def head_product_type(self,loc):
        '''快捷键搜索'''
        result =self.driver.find_element(*loc).text
        self.driver.find_element(*loc).click()
        return result

    def product_type(self,type_loc,text):
        '''产品类型搜索'''
        loc = self.driver.find_element(*type_loc)
        action = ActionChains(self.driver)
        action.move_to_element(loc).perform()
        self.driver.find_element(By.LINK_TEXT,text).click()

    def product(self,product_loc):
        '''点击查看产品详情'''
        self.driver.find_element(*product_loc).click()

    def add_shopcar(self):
        '''商品详情页加入购物车'''
        self.driver.find_element(*self.locator_add_shopcar).click()

    def search_add_shopcar(self,keyword,product_loc):
        '''搜索添加购物车'''
        self.font_home_page()
        self.key_word(keyword)
        self.product(product_loc)
        result = self.driver.title
        self.add_shopcar()
        return result

    def quick_add_shopcar(self,loc,product_loc):
        '''快速筛选加入购物车'''
        self.font_home_page()
        expect = self.head_product_type(loc)
        self.product(product_loc)
        actual = self.driver.title
        self.add_shopcar()
        return expect,actual

    def type_add_shopcar(self,type_loc,text,product_loc):
        '''类型筛选加入购物车'''
        self.font_home_page()
        self.product_type(type_loc,text)
        self.product(product_loc)
        result = self.driver.title
        self.add_shopcar()
        return result