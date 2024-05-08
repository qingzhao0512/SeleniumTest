'''
Author: qingzhao0512 qingzhao0512@gmail.com
Date: 2024-05-06 17:31:33
LastEditors: qingzhao0512 qingzhao0512@gmail.com
LastEditTime: 2024-05-08 20:27:48
FilePath: \SeleniumTest\demo5.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

# 节点交互

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

# 使用正确的变量名，并确保CSS选择器正确
input_first = browser.find_element(
    By.CSS_SELECTOR, '.rax-textinput.rax-textinput-placeholder-6.searchbar-input')
input_first.send_keys('iPhone')  # 使用正确的变量名
time.sleep(1)
input_first.clear()
input_first.send_keys('iPad')

# 修正按钮的CSS选择器
button = browser.find_element(
    By.CSS_SELECTOR, '.rax-text-v2.search-button-text')  # 修正选择器格式
button.click()

# 在结束前打印一些输出，可以帮助调试
print("Search completed")

# 最后记得关闭浏览器
browser.close()
