# -*- coding: UTF-8 -*-
# @Time : 2022/3/3 16:06
# @File : first_ddt_case.py
# @Software : PyCharm
import ddt
# 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
import sys
sys.path.append("D:\\PycharmProjects\\coachbacktest")
import traceback
import os
'''
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
'''
import time
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
from util.excel_util import ExcelUtil

ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http:www.5itest.cn/register")
        self.register = RegisterBusiness(self.driver)
    def tearDown(self):
        time.sleep(2)
        #if sys.exc_info()[0]:
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
    '''
    @ddt.data(
        ['14', 'xiaoxiao', '123456', '1234', 'user_email_error', '请输入有效的电子邮件地址'],
        ['@qq.com', 'xiaoxiao', '123456', '1234', 'user_email_error', '请输入有效的电子邮件地址'],
        ['132435@qq.com', 'xiaoxiao', '123456', '1234', 'user_email_error', '请输入有效的电子邮件地址']
    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self, data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.register.register_function(email, username, password, code, assertCode, assertText)
        return self.assertFalse(email_error, "测试失败")

if __name__ == '__main__':
    file_path = "../report/" + "first_case1.html"
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report1", description=u'第一次测试报告1', verbosity=2)
    runner.run(suite)
