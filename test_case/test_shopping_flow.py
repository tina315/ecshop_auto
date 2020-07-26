'''购物用例类'''
import unittest
from data.base_data import DATA_PATH
from lib.get_login_data import ReadCsv
from page.home_page import HomePage
from page.login_page import LoginPage
from page.pay_page import PayPage
from page.register_page import RegisterPage
from page.shopcart_page import ShopCartPage
from page.user_center_page import UserCenterPage
from test_case.test_base import BaseTestCase


class ShoppingTestCase(BaseTestCase):
    '''购物用例类'''
    def test_shopping_flow(self): #已购物过的会员购物流程
        '''购物流程用例'''
        #登录
        file_name = DATA_PATH + r'\data_login.csv'
        data = ReadCsv().read_login_data(file_name)
        username = data[0][0]
        password = data[0][1]
        login = LoginPage(self.driver)
        actual = login.login(username,password)
        self.assertEqual(username, actual)
        #添加购物车
        index = '2'
        text = '衬衫'
        product_index = '2'
        action = HomePage(self.driver)
        actual = action.type_add_shopcart(index,text,product_index)
        self.assertIn(text, actual)
        #进入结算
        shopcart = ShopCartPage(self.driver)
        shopcart.go_to_pay()
        #结算订单
        send_way_index = 0
        pay_way_index = 0
        pay = PayPage(self.driver)
        actual =pay.pay_order(send_way_index,pay_way_index)
        self.assertIn('step=done', actual)

    def test_first_shopping_flow(self): #未购物过的会员购物流程
        '''购物流程用例'''
        #登录
        file_name = DATA_PATH + r'\data_login.csv'
        data = ReadCsv().read_login_data(file_name)
        username = data[1][0]
        password = data[1][1]
        login = LoginPage(self.driver)
        actual = login.login(username,password)
        self.assertEqual(username, actual)
        #添加收货地址
        file_name = DATA_PATH + r'\data_addr.csv'
        data = ReadCsv().read_addr_data(file_name)
        addr = UserCenterPage(self.driver)
        addr.add_addr(*data[1])
        #添加购物车
        index = '2'
        text = '衬衫'
        product_index = '2'
        action = HomePage(self.driver)
        actual = action.type_add_shopcart(index,text,product_index)
        self.assertIn(text, actual)
        #进入结算
        shopcart = ShopCartPage(self.driver)
        shopcart.go_to_pay()
        shopcart.select_addr()
        #结算订单
        send_way_index = 0
        pay_way_index = 0
        pay = PayPage(self.driver)
        actual =pay.pay_order(send_way_index,pay_way_index)
        self.assertIn('step=done', actual)

    def test_new_shopping_flow(self): #新注册的会员购物流程
        '''购物流程用例'''
        #注册
        username = 'wangdd'
        email = username + '@126.com'
        password = '123456'
        confirm_password = password
        register = RegisterPage(self.driver)
        actual = register.register(username,email,password,confirm_password)
        self.assertEqual(username, actual)
        #添加收货地址
        file_name = DATA_PATH + r'\data_addr.csv'
        data = ReadCsv().read_addr_data(file_name)
        addr = UserCenterPage(self.driver)
        addr.add_addr(*data[1])
        #添加购物车
        index = '2'
        text = '衬衫'
        product_index = '2'
        action = HomePage(self.driver)
        actual = action.type_add_shopcart(index,text,product_index)
        self.assertIn(text, actual)
        #进入结算
        shopcart = ShopCartPage(self.driver)
        shopcart.go_to_pay()
        shopcart.select_addr()
        #结算订单
        send_way_index = 0
        pay_way_index = 0
        pay = PayPage(self.driver)
        actual =pay.pay_order(send_way_index,pay_way_index)
        self.assertIn('step=done', actual)


if __name__ == '__main__':
    unittest.main()
