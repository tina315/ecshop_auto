'''测试用例基类'''
import unittest
from driver.browser import chrome_driver


class BaseTestCase(unittest.TestCase):
    '''测试用例基类'''
    def setUp(self):
        '''搭建环境'''
        self.driver = chrome_driver()

    def tearDown(self):
        '''清理环境'''
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
