'''
Author: qingzhao0512 qingzhao0512@gmail.com
Date: 2024-05-06 17:31:33
LastEditors: qingzhao0512 qingzhao0512@gmail.com
LastEditTime: 2024-05-08 20:55:34
FilePath: \SeleniumTest\demo9.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 获取文本值


from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://spa2.scrape.center//'
browser.get(url)
input = browser.find_element(By.CLASS_NAME, 'logo-image')
print('input', input, '\n')               # 打印出WebElement对象，显示了它的会话ID和元素ID
# 这一行打印的是该元素的可见文本。对于大多数HTML元素，如<div>、<span>、<a>等，.text属性会返回其中包含的所有文本内容。这对于测试网页上显示的文本或进行内容抓取非常有用。对于<img>元素，如您的示例中所用的'logo-image'类，通常不包含可见文本。因此，input.text很可能返回一个空字符串，因为图像标签(<img>)内部不包含文本内容。
print('input.text', input.text, '\n')

print('input.id', input.id, '\n')
print('input.location', input.location, '\n')
print('input.tag_name,', input.tag_name, '\n')
print('input.size', input.size, '\n')
browser.quit()
