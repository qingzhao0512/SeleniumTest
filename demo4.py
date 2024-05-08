'''
Author: qingzhao0512 qingzhao0512@gmail.com
Date: 2024-05-06 17:31:33
LastEditors: qingzhao0512 qingzhao0512@gmail.com
LastEditTime: 2024-05-08 20:20:20
FilePath: \SeleniumTest\demo4.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 查找左侧导航条


from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

# 使用正确的方法和CSS选择器
lis = browser.find_elements(By.CSS_SELECTOR, '.rax-view.category-wrapper')
print(lis)
browser.close()
