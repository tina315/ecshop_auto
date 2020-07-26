'''用户中心用例类'''
import unittest
from data.base_data import DATA_PATH
from lib.get_login_data import ReadCsv
from page.login_page import LoginPage
from page.user_center_page import UserCenterPage
from test_case.test_base import BaseTestCase


class UserCenterPageTestCase(BaseTestCase):
    '''用户中心用例类'''
    def test_add_addr(self):
        '''添加收货地址用例'''
        file_name = DATA_PATH + r'\data_login.csv'
        data = ReadCsv().read_login_data(file_name)
        username = data[-1][0]
        password = data[-1][1]
        login = LoginPage(self.driver)
        actual = login.login(username,password)
        self.assertEqual(username, actual)
        file_name = DATA_PATH + r'\data_addr.csv'
        data = ReadCsv().read_addr_data(file_name)
        addr = UserCenterPage(self.driver)
        addr.add_addr(*data[1])


if __name__ == '__main__':
    unittest.main()
