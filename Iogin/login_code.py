# -*- coding: UTF-8 -*-
# @Time : 2022/2/8 13:11
# @File : login_code.py
# @Software : PyCharm
import random
from PIL import Image
import pytesseract
from selenium import webdriver
import time

driver = webdriver.Chrome()

# 浏览器初始化
def drvier_init():
    url = "http://coachbacktest.chaolu.com.cn/#/doLogin"
    driver.get("http://coachbacktest.chaolu.com.cn/#/doLogin")
    driver.maximize_window()
    time.sleep(5)

# 获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element
# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890qwertyuiopasdfghjklzxcvbnm', 8))
    return user_info
# 获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width']+left
    height = code_element.size['height']+top
    im = Image.open(file_name)
    img = im.crop(left, top, right, height)
    img.save(file_name)
# 解析图片获取验证码
def code_online(file_name):
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
    return text
# 运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info + "@163.com"
    file_name = "test02.png"
    drvier_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("123456")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register_btn").click()
    driver.close()

if __name__ == '__main__':
    run_main()