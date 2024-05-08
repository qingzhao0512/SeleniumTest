'''
Author: qingzhao0512 qingzhao0512@gmail.com
Date: 2024-05-06 17:31:33
LastEditors: qingzhao0512 qingzhao0512@gmail.com
LastEditTime: 2024-05-08 18:03:58
FilePath: \SeleniumTest\demo3.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
""" from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.CLASS_NAME, 'rax-textinput rax-textinput-placeholder-6 searchbar-input')
input_first.send_keys('iPhone')
input_first.send_keys(Keys.ENTER)


# print(input_first)
browser.close() """



# 上述代码跑不通，因为不是CLASS_NAME，而是CSS_SELECTOR

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

# 使用CSS选择器来定位有多个类的元素
input_first = browser.find_element(By.CSS_SELECTOR, '.rax-textinput.rax-textinput-placeholder-6.searchbar-input')
input_first.send_keys('iPhone')
input_first.send_keys(Keys.ENTER)

# 打印一些输出可能帮助调试
print(input_first)  # 查看找到的元素
print(browser.current_url)  # 打印当前URL

browser.close()





""" 下面是ChatGPT对于CLASS_NAME，和CSS_SELECTOR的解释
理解何时使用 `By.CLASS_NAME` 和何时使用 `By.CSS_SELECTOR` 是自动化测试中的一个重要部分。这两者的主要区别在于如何选择HTML元素以及它们各自的限制。以下是详细的解释和指导：

### By.CLASS_NAME
- **用途**：当您想通过单个类名定位元素时使用`By.CLASS_NAME`。
- **限制**：只能使用一个类名。如果一个元素具有多个类名，您不能将它们一起作为参数传递给`By.CLASS_NAME`。例如，如果一个元素的类属性是`class="button primary large"`，您只能选择其中一个，如`"primary"`来定位这个元素。
- **示例代码**：
  ```python
  # 正确的使用方法
  element = driver.find_element(By.CLASS_NAME, 'primary')
  ```

### By.CSS_SELECTOR
- **用途**：`By.CSS_SELECTOR`更通用，可以用来选择具有特定属性的单个或多个元素。它不仅限于类名，还可以通过ID、属性、组合选择器等来定位元素。
- **优势**：可以用来定位具有多个类名的元素。您只需用`.`连接每个类名，就像在CSS中一样。
- **示例代码**：
  ```python
  # 用来选择具有多个类名的元素
  element = driver.find_element(By.CSS_SELECTOR, '.button.primary.large')
  # 使用其他属性进行定位
  element = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
  ```

### 何时使用By.CSS_SELECTOR而不是By.CLASS_NAME
- 当您需要选择的元素具有多个类名时，应该使用`By.CSS_SELECTOR`。
- 当您需要更复杂的选择器，比如基于元素的层次结构或特定属性（例如类型、属性值等）选择元素时，也应该使用`By.CSS_SELECTOR`。

### 总结
- **简单选择单一类名**：使用`By.CLASS_NAME`。
- **需要更复杂或精确的选择器**，或**元素具有多个类名**：使用`By.CSS_SELECTOR`。

希望这样的解释能帮助您更清楚地理解何时使用这两种选择器。如果您在自动化脚本中需要处理具有多个类名的元素或更复杂的选择情况，通常`By.CSS_SELECTOR`是更灵活和强大的选择。 """