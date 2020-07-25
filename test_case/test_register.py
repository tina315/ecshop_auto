'''注册用例类'''
import unittest
from page.register_page import RegisterPage
from test_case.test_base import BaseTestCase


class RegisterTestCase(BaseTestCase):
    '''注册用例类'''
    def test_register(self):
        '''用户注册用例'''
        username = 'wanguu'
        email = username + '@126.com'
        password = '123456'
        confirm_password = password
        register = RegisterPage(self.driver)
        actual = register.register(username,email,password,confirm_password)
        self.assertEqual(username, actual)

if __name__ == '__main__':
    unittest.main()
