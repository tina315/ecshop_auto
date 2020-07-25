'''前台首页类'''
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page.base_page import BasePage


class HomePage(BasePage):
    '''前台首页类'''

    #定位器
    locator_keyword = (By.ID,'keyword')
    locator_shopcart = (By.XPATH,'//li[@id="ECS_CARTINFO"]/a')
    locator_add_shopcart = (By.XPATH,'//form[@id="ECS_FORMBUY"]/ul[3]/li[2]/a/img')

    def get_in_shopcart(self):
        '''首页进入购物车'''
        self.driver.find_element(*self.locator_shopcart).click()
        result = self.driver.title
        return result

    def key_word(self,keyword):
        '''关键字搜索'''
        self.driver.find_element(*self.locator_keyword).clear()
        self.driver.find_element(*self.locator_keyword).send_keys(keyword)
        self.driver.find_element(*self.locator_keyword).send_keys(Keys.ENTER)

    def head_product_type(self,index):
        '''快捷键搜索'''
        xpath = '//div[@class="menu"]/a[' + index + ']'
        loc = (By.XPATH,xpath)
        result =self.driver.find_element(*loc).text
        self.driver.find_element(*loc).click()
        return result

    def product_type(self,index,text):
        '''产品类型搜索'''
        xpath = '//div[@id="category_tree"]/dl/div[' + index +']/div/a'
        type_loc = (By.XPATH,xpath)
        loc = self.driver.find_element(*type_loc)
        action = ActionChains(self.driver)
        action.move_to_element(loc).perform()
        self.driver.find_element(By.LINK_TEXT,text).click()

    def product(self,product_index):
        '''点击查看产品详情'''
        #By.XPATH,'//form[@name="compareForm"]/div/div[2]/a/img'
        xpath = '//form[@name="compareForm"]/div/div[' + product_index + ']/a/img'
        product_loc = (By.XPATH,xpath)
        self.driver.find_element(*product_loc).click()

    def add_shopcart(self):
        '''商品详情页加入购物车'''
        self.driver.find_element(*self.locator_add_shopcart).click()

    def search_add_shopcart(self,keyword,product_index):
        '''搜索添加购物车'''
        self.font_home_page()
        self.key_word(keyword)
        self.product(product_index)
        result = self.driver.title
        self.add_shopcart()
        return result

    def quick_add_shopcart(self,index,product_index):
        '''快速筛选加入购物车'''
        self.font_home_page()
        expect = self.head_product_type(index)
        self.product(product_index)
        actual = self.driver.title
        self.add_shopcart()
        return expect,actual

    def type_add_shopcart(self,index,text,product_index):
        '''类型筛选加入购物车'''
        self.font_home_page()
        self.product_type(index,text)
        self.product(product_index)
        result = self.driver.title
        self.add_shopcart()
        return result