# -*- coding: UTF-8 -*-
# @Time : 2022/2/10 13:12
# @File : unittest_case02.py
# @Software : PyCharm
import unittest

class FirstCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有case的前置")

    @classmethod
    def tearDwonClass(cls):
        print("所有case的后置")

    def setup(self):
        print("前置")
    def tearDown(self):
        print("后置")
    @unittest.skip
    def testfirst001(self):
        print("第一个case")
    def testfirst002(self):
        print("第二个case")
    def testfirst003(self):
        print("第二个case")


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst02'))
    unittest.TextTestRunner.run(suite)