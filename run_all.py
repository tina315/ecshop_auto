'''批量执行用例生成报告'''
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from data.base_data import REPORT_PATH

test_dir = "test_case"
test_report = REPORT_PATH + '-'
#批量执行用例
discover = unittest.defaultTestLoader.discover(start_dir=test_dir,
                                               pattern='test*.py',
                                               top_level_dir=None)
times = time.strftime('%Y%m%d%H%M%S',time.localtime())
report_file = test_report + times + '-result.html'
with open(report_file,'wb+') as f: #二进制没有编码格式
    runner = HTMLTestRunner(stream=f,
                            title='EcshopAutoTest',
                            description='EcshopAutoTestReport')
    runner.run(discover)