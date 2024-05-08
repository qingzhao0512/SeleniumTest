'''
Author: qingzhao0512 qingzhao0512@gmail.com
Date: 2024-05-06 17:31:33
LastEditors: qingzhao0512 qingzhao0512@gmail.com
LastEditTime: 2024-05-08 20:40:18
FilePath: \SeleniumTest\demo8.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 获取节点信息
# Selenium 的更新版本（4.x 版本开始）已经将这些方法进行了一些调整，统一了元素查找的接口。您应该使用 find_element 方法，并配合 By.CLASS_NAME 来定位元素。

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://spa2.scrape.center//'
browser.get(url)
logo = browser.find_element(By.CLASS_NAME, 'logo-image')
print(logo)
print(logo.get_attribute('src'))       # 打印源属性
