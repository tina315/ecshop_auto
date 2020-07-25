'''添加商品用例类'''
import unittest
from data.base_data import DATA_PATH
from lib.get_login_data import ReadCsv
from page.add_product_page import AddProductPage
from page.admin_page import AdminPage
from test_case.test_base import BaseTestCase


class AddProductTestCase(BaseTestCase):
    '''添加商品用例类'''
    def test_add_product(self):
        '''添加商品用例'''
        #登录后台
        file_name = DATA_PATH + r'\data_admin.csv'
        data = ReadCsv().read_admin_data(file_name)
        name = data[0][0]
        password = data[0][1]
        admin = AdminPage(self.driver)
        actual = admin.admin_login(name,password)
        self.assertIn('index', actual)
        #添加商品
        product_name = 'strawberry_cake'
        value = '533'
        price = '20'
        sdate = '2020-07-01'
        edate = '2020-12-31'
        sale_price = '2.99'
        path = DATA_PATH + r'\logo.gif'
        addproduct = AddProductPage(self.driver)
        actual = addproduct.add_product(product_name,value,price,sdate,edate,sale_price,path)
        self.assertEqual(product_name, actual)


if __name__ == '__main__':
    unittest.main()
