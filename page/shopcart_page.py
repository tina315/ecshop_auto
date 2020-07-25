'''购物车页面类'''
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class ShopCartPage(BasePage):
    '''购物车页面类'''

    #定位器
    locator_back_to_shopping = (By.XPATH,'//div[@class="flowBox"]/table/tbody/tr/td[1]/a/img')
    locator_go_to_pay = (By.XPATH,'//div[@class="flowBox"]/table/tbody/tr/td[2]/a/img')
    locator_clear_shopcart = (By.XPATH,'//form[@id="formCart"]/table[2]/tbody/tr/td[2]/input[1]')
    locator_update_shopcart = (By.XPATH,'//form[@id="formCart"]/table[2]/tbody/tr/td[2]/input[2]')

    def back_to_shopping(self):
        '''继续购物'''
        self.driver.find_element(*self.locator_back_to_shopping).click()

    def go_to_pay(self):
        '''进入结算'''
        self.driver.find_element(*self.locator_go_to_pay).click()

    def clear_shopcart(self):
        '''清空购物车'''
        self.driver.find_element(*self.locator_clear_shopcart).click()

    def update_shopcart(self):
        '''清空购物车'''
        self.driver.find_element(*self.locator_update_shopcart).click()

    def edit_product_num(self,index,num):
        '''修改商品数量'''
        xpath = '//form[@id="formCart"]/table[1]/tbody/tr[' + index + ']/td[5]/input'
        loc = (By.XPATH,xpath)
        self.driver.find_element(*loc).clear()
        self.driver.find_element(*loc).send_keys(num)

    def delete_product(self,index):
        '''删除商品'''
        xpath = '//form[@id="formCart"]/table[1]/tbody/tr[' + index + ']/td[7]/a'
        loc = (By.XPATH,xpath)
        self.driver.find_element(*loc).click()
        self.driver.switch_to.alert.accept()