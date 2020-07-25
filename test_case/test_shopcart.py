'''购物车测试用例类'''
import unittest
from page.home_page import HomePage
from page.shopcart_page import ShopCartPage
from test_case.test_base import BaseTestCase


class ShopCartTestCase(BaseTestCase):
    '''购物车测试用例类'''
    def test_shopcart(self):
        '''购物车测试用例'''
        shop = HomePage(self.driver)
        shop.open_front_page()
        actual = shop.get_in_shopcart()
        self.assertIn('购物流程', actual)
        shopcart = ShopCartPage(self.driver)
        shopcart.go_to_pay()


if __name__ == '__main__':
    unittest.main()
