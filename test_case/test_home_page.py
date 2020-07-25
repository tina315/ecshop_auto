'''前台首页用例类'''
import unittest
from selenium.webdriver.common.by import By
from page.home_page import HomePage
from test_case.test_base import BaseTestCase


class HomePageTestCase(BaseTestCase):
    '''前台首页用例类'''

    #定位器


    def test_search_add_shopcar(self):
        '''关键词搜索加入购物车用例'''
        keyword = '毛衣'
        product_index = '2'
        action = HomePage(self.driver)
        action.open_front_page()
        actual = action.search_add_shopcart(keyword,product_index)
        self.assertIn(keyword, actual)

    def test_quick_add_shopcar(self):
        '''快捷筛选加入购物车用例'''
        index = '2'
        product_index = '2'
        action = HomePage(self.driver)
        action.open_front_page()
        expect,actual = action.quick_add_shopcart(index,product_index)
        self.assertIn(expect,actual)

    def test_type_add_shopcar(self):
        '''类型筛选加入购物车用例'''
        index = '2'
        text = '衬衫'
        product_index = '2'
        action = HomePage(self.driver)
        action.open_front_page()
        actual = action.type_add_shopcart(index,text,product_index)
        self.assertIn(text, actual)

    def test_get_in_shopcar(self):
        '''前台首页进入购物车'''
        action = HomePage(self.driver)
        action.open_front_page()
        actual = action.get_in_shopcart()
        self.assertIn('购物流程', actual)


if __name__ == '__main__':
    unittest.main()
