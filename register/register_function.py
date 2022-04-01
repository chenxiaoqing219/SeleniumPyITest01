# -*- coding: UTF-8 -*-
# @Time : 2022/2/8 16:35
# @File : register_function.py
# @Software : PyCharm
import sys
sys.path.append('coachbacktest')
from selenium import webdriver
import time
import random
from PIL import Image
from base.find_element import FindElement
import pytesseract

class RegisterFunction(object):
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)
    # 获取driver并且打开url
    def get_driver(self, url, i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.get(url)
        driver.maximize_window()
        return driver
    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)
    # 定位用户信息，获取element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890qwertyuiopasdfghjklzxcvbnm', 8))
        return user_info

    # 获取图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        # print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    # 解析图片获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        im = Image.open(file_name)
        im = im.convert('L')
        threshold = 127
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        im = im.point(table, '1')
        text = pytesseract.image_to_string(im)
        print(text)
        return text


    def main(self, i):
        user_name_info = self.get_range_user()
        user_email = user_name_info + "@163.com"
        file_name = "D:/PycharmProjects/coachbacktest/Image/test001.png"
        code_text = self.code_online(file_name)
        self.send_user_info('user_email', user_email)
        self.send_user_info('user_name', user_name_info)
        self.send_user_info('password', '111111')
        self.send_user_info('code_text', code_text)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element("code_text_error")
        if code_error == None:
            print("验证码正确")
        else:
            code_error_png = 'codeerror_' + str(i) + '.png'
            self.driver.save_screenshot("../Image/"+code_error_png)
        time.sleep(5)
        self.driver.close()
        time.sleep(5)

if __name__ == '__main__':
    for i in range(3):
        register_function = RegisterFunction('http://www.5itest.cn/register', i)
        register_function.main(i)