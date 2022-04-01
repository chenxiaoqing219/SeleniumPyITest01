# -*- coding: UTF-8 -*-
# @Time : 2022/3/10 16:10
# @File : keyword_case.py
# @Software : PyCharm
import sys
sys.path.append('D:\\PycharmProjects\\coachbacktest')
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil('D:\PycharmProjects\coachbacktest\config\keyword.xls')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_col_value(i, 3)
                if is_run == 'yes':
                    method = handle_excel.get_col_value(i, 4)
                    send_value = handle_excel.get_col_value(i, 5)
                    handle_value = handle_excel.get_col_value(i, 6)
                    #if send_value:
                    self.run_method(method, send_value, handle_value)
        # 拿到行数
        # 循环行数，去执行每一行的case
        # 是否执行
            # 拿到执行方法
            # 拿到操作值
            # 拿到输入数据
            # if 是否有输入数据
                # 执行方法（输入数据，操作元素）
            # if 没有输入数据
                # 执行方法（操作元素）
    def run_method(self, method, send_value, handle_value):
        method_value = getattr(self.action_method, method)
        if send_value:
            method_value(send_value, handle_value)
        else:
            method_value(handle_value)

if __name__ == '__main__':
    kc = KeywordCase()
    kc.run_main()