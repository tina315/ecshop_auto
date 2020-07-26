'''基础数据'''
import os

front_url = 'http://192.168.1.40/upload/'
back_url = 'http://192.168.1.40/upload/admin/'
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASE_PATH = BASE_PATH + r'\case'
DATA_PATH = BASE_PATH + r'\data'
DRIVER_PATH = BASE_PATH + r'\driver'
LIB_PATH = BASE_PATH + r'\lib'
PAGE_PATH = BASE_PATH + r'\page'
TEST_CASE_PATH = BASE_PATH + r'\test_case'
REPORT_PATH = BASE_PATH + r'\report'