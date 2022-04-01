# -*- coding: UTF-8 -*-
# @Time : 2022/3/3 14:51
# @File : data_test.py
# @Software : PyCharm
import ddt
import unittest
@ddt.ddt
class DateTest(unittest.TestCase):
    def setUp(self) -> None:
        print("这是个setup")
    def tearDown(self) -> None:
        print("这是个teardown")
    @ddt.data(
        ["1", "2"],
        ["3", "4"],
        ["5", "6"],
        [1, 2],
        [3, 4],
        [5, 6]

    )
    @ddt.unpack
    def test_add(self, a, b):

        print(a + b)

if __name__ == '__main__':
    unittest.main()