# -*- coding: UTF-8 -*-
# @Time : 2022/2/9 15:04
# @File : register_business.py
# @Software : PyCharm
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)
    def user_base(self,email,user_name,password,code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(user_name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()

    def register_success(self):
        if self.register_h.get_register_text() == None:
            return True
        else:
            return False
    # 执行操作
    def register_email_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('email_error', "请输入有效的电子邮件地址") == None:
            #print("邮箱检验不成功")
            return True
        else:
            return False

    def register_function(self, email, username, password, code, assertCode, assertText):
        self.user_base(email, username, password, code)
        if self.register_h.get_user_text(assertCode, assertText) == None:
            #print("邮箱检验不成功")
            return True
        else:
            return False
    def register_name_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('name_error', "字符长度必须大于等于4，一个中文字算2个字符") == None:
            #print("用户名检验不成功")
            return True
        else:
            return False
    def register_password_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('password_error', "最少需要输入 5 个字符") == None:
            #print("密码检验不成功")
            return True
        else:
            return False
    def register_code_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('code_text_error', "验证码错误") == None:
            #print("验证码检验不成功")
            return True
        else:
            return False