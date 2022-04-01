# -*- coding: UTF-8 -*-
# @Time : 2022/2/9 14:44
# @File : register_handle.py
# @Software : PyCharm
from page.register_page import RegisterPage
from util.get_code import GetCode
class RegisterHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.regiter_p = RegisterPage(self.driver)
    # 输入邮箱
    def send_user_email(self, email):
        self.regiter_p.get_email_element().send_keys(email)

    # 输入用户名
    def send_user_name(self, username):
        self.regiter_p.get_username_element().send_keys(username)

    # 输入密码
    def send_user_password(self, password):
        self.regiter_p.get_password_element().send_keys(password)

    # 输入验证码
    def send_user_code(self, file_name):
        get_code_text = GetCode(self.driver)
        code = get_code_text.code_online(file_name)
        self.regiter_p.get_code_element().send_keys(code)

    # 获取文字信息
    def get_user_text(self, info, user_info):
        try:
            if info == 'user_email_error':
                text = self.regiter_p.get_email_error_element().text
            elif info == 'user_name_error':
                text = self.regiter_p.get_name_error_element().text
            elif info == 'password_error':
                text = self.regiter_p.get_password_error_element().text
            else:
                text = self.regiter_p.get_code_error_element().text
        except:
            text = None
        #print(text)
        return text

    # 点击注册按钮
    def click_register_button(self):
        self.regiter_p.get_button_element().click()

    # 获取注册按钮文字
    def get_register_text(self):
        self.regiter_p.get_button_element().text
