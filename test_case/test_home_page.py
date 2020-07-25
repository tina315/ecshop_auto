'''前台首页用例类'''
import unittest
from selenium.webdriver.common.by import By
from page.home_page import HomePage
from test_case.test_base import BaseTestCase


class HomePageTestCase(BaseTestCase):
    '''前台首页用例类'''

    #定位器
    locator_head_product_type = (By.XPATH,'//div[@class="menu"]/a[2]')
    locator_product_type = (By.XPATH,'//div[@id="HandleLI2_2"]/a')
    locator_product = (By.XPATH,'//form[@name="compareForm"]/div/div[2]/a/img')

    def test_search_add_shopcar(self):
        '''关键词搜索加入购物车用例'''
        keyword = '毛衣'
        product_loc = self.locator_product
        action = HomePage(self.driver)
        action.open_front_page()
        actual = action.search_add_shopcar(keyword,product_loc)
        self.assertIn(keyword, actual)

    def test_quick_add_shopcar(self):
        '''快捷筛选加入购物车用例'''
        loc = self.locator_head_product_type
        product_loc = self.locator_product
        action = HomePage(self.driver)
        action.open_front_page()
        expect,actual = action.quick_add_shopcar(loc,product_loc)
        self.assertIn(expect,actual)

    def test_type_add_shopcar(self):
        '''类型筛选加入购物车用例'''
        type_loc = self.locator_product_type
        text = '衬衫'
        product_loc = self.locator_product
        action = HomePage(self.driver)
        action.open_front_page()
        actual = action.type_add_shopcar(type_loc,text,product_loc)
        self.assertIn(text, actual)


if __name__ == '__main__':
    unittest.main()
