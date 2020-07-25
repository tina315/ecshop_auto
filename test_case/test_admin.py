'''后台管理员登录用例类'''
import unittest
from data.base_data import DATA_PATH
from lib.get_login_data import ReadCsv
from page.admin_page import AdminPage
from test_case.test_base import BaseTestCase


class AdminLoginTestCase(BaseTestCase):
    '''后台管理员登录用例类'''
    def test_admin_login(self):
        '''管理员登录用例'''
        file_name = DATA_PATH + r'\data_admin.csv'
        data = ReadCsv().read_admin_data(file_name)
        name = data[0][0]
        password = data[0][1]
        admin = AdminPage(self.driver)
        actual = admin.admin_login(name,password)
        self.assertIn('index', actual)


if __name__ == '__main__':
    unittest.main()
