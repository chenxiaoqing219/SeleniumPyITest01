# -*- coding: UTF-8 -*-
# @Time : 2022/2/9 14:39
# @File : first_case.py
# @Software : PyCharm
#import os
#import sys
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import time
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
from log.user_log import UserLog


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name = "D:/PycharmProjects/coachbacktest/Image/test001.png"
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http:www.5itest.cn/register")
        self.logger.info("this is chrome")

        self.register = RegisterBusiness(self.driver)
    def tearDown(self):
        time.sleep(2)
        #if sys.exc_info()[0]:
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"D:/PycharmProjects/coachbacktest/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_register_email_error(self):
        email_error = self.register.register_email_error('122', '22222', '33333', self.file_name)
        return self.assertFalse(email_error, "测试失败")
    def test_register_username_error(self):
        name_error = self.register.register_name_error('1111@qq.com', '2', '33333', self.file_name)
        return self.assertFalse(name_error, "测试失败")
    def test_register_code_error(self):
        code_error = self.register.register_code_error('1111@qq.com', '22222', '3111', self.file_name)
        return self.assertFalse(code_error, "测试失败")
    def test_register_password_error(self):
        password_error = self.register.register_password_error('1111@qq.com', '2222a', '3', self.file_name)
        return self.assertFalse(password_error, "测试失败")
    def test_register_success(self):
        success = self.register.user_base('1111@qq.com', '22222', '33333', self.file_name)
        return self.assertFalse(success)
'''
def main():
    first = FirstCase()
    first.test_register_email_error()
    first.test_register_username_error()
    first.test_register_password_error()
    first.test_register_code_error()
    first.test_register_success()
'''
if __name__ == '__main__':
    #unittest.main()
    file_path = 'D:/PycharmProjects/coachbacktest/report/first_case.html'
    #file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_register_email_error'))
    suite.addTest(FirstCase('test_register_username_error'))
    suite.addTest(FirstCase('test_register_code_error'))
    suite.addTest(FirstCase('test_register_password_error'))
    suite.addTest(FirstCase('test_register_success'))
    #unittest.TextTestRunner.run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report", description=u'第一次测试报告', verbosity=2)
    runner.run(suite)