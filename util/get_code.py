# -*- coding: UTF-8 -*-
# @Time : 2022/3/3 10:35
# @File : get_code.py
# @Software : PyCharm
from PIL import Image
import pytesseract
import time
class GetCode:
    def __init__(self, driver):
        self.driver = driver
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        # print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(2)

    # 解析图片获取验证码
    def code_online(self, file_name):
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
        time.sleep(2)
        return text