'''登录用例类'''
import unittest
from data.base_data import DATA_PATH
from page.login_page import LoginPage
from test_case.test_base import BaseTestCase
from lib.get_login_data import ReadCsv

class LoginTestCase(BaseTestCase):
    '''登录用例类'''
    def test_login(self):
        file_name = DATA_PATH + r'\data_login.csv'
        data = ReadCsv().read_login_data(file_name)
        username = data[0][0]
        password = data[0][1]
        login = LoginPage(self.driver)
        actual = login.login(username,password)
        self.assertEqual(username, actual)


if __name__ == '__main__':
    unittest.main()
