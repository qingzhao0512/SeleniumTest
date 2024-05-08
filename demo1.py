'''
Author: qingzhao0512 qingzhao0512@gmail.com
Date: 2024-05-06 17:31:33
LastEditors: qingzhao0512 qingzhao0512@gmail.com
LastEditTime: 2024-05-08 17:49:01
FilePath: \SeleniumTest\demo1.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from selenium import webdriver                                # webdriver是Selenium提供的一个用于控制和操作浏览器的接口。
from selenium.webdriver.common.by import By                   # 导入By类，这个类包含了一系列用于指定HTML元素的方法，如ID, CLASS_NAME等，用于帮助Selenium找到网页上的元素。
from selenium.webdriver.common.keys import Keys               # 导入Keys类，这个类提供了键盘按键的常量，如ENTER, ESC等，用于在自动化脚本中模拟键盘操作。
from selenium.webdriver.support import expected_conditions as EC    # 导入expected_conditions，通常简称为EC。这个模块提供了一系列的方法用于等待某些条件的满足，比如元素可见、元素可点击等。
from selenium.webdriver.support.wait import WebDriverWait     # 导入WebDriverWait类，这个类是用于等待某个条件成立或直到超时。

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    # 使用 By.ID 替换 find_element_by_id
    input = browser.find_element(By.ID, 'kw')        # 找到百度首页上搜索输入框的元素。这里使用By.ID，'kw'是该输入框的ID。
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)       # 这行代码使用send_keys方法向网页元素发送按键事件。Keys.ENTER代表键盘上的"Enter"键。
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))     # 等待直到ID为content_left的元素出现在DOM（Document Object Model），即文档对象模型中。content_left是百度搜索结果页面左侧内容的容器ID。
    print(browser.current_url)                       # 打印当前浏览器的URL，此时应该是百度的搜索结果页面。
    print(browser.get_cookies())                     # 打印当前页面的cookies信息。
    print(browser.page_source)                       # 打印当前页面的HTML源码。
finally:                          # 前面用了try，然后无论之前的代码块执行成功与否，最终都会关闭浏览器窗口。这是清理资源的重要步骤，防止留下未关闭的浏览器窗口。
    browser.close()




""" ### DOM的解释
DOM是文档对象模型（Document Object Model）的缩写，它是一个跨平台和语言独立的接口，允许程序和脚本动态地访问和更新文档的内容、结构和样式。在Web开发中，DOM通常指的是网页文档的模型。

网页被浏览器解析后，浏览器会根据HTML文档创建出一个DOM树。DOM树是由节点组成的，这些节点代表了文档中的各个元素，比如文本块、图片、链接、表格等。通过DOM，JavaScript和其他编程语言能够进行如下操作：

- **检索元素**：可以按照ID、类名、标签名等属性查找页面上的元素。
- **添加或删除元素**：可以动态地添加或删除页面上的元素，改变页面结构。
- **修改元素属性**：可以改变元素的属性，比如样式、内容等。
- **响应事件**：可以为元素添加事件响应函数，使页面具有交互性。

### 等待DOM中的元素出现
在自动化测试或网页抓取中，有时候页面元素是动态加载的，即它们不会在页面最初加载时立即出现，而是在某些操作（如点击、滚动等）或异步请求完成后才会被添加到DOM树中。因此，在尝试对这些元素进行操作之前，需要确保它们已经存在于DOM中。

Selenium通过`WebDriverWait`和`expected_conditions`提供了等待机制，使得可以等待特定条件成立。在您提到的代码片段中：

```python
wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
```
这行代码将等待直到ID为`content_left`的元素在DOM中出现。`presence_of_element_located`是一个条件（provided by `expected_conditions`），它会定期检查指定元素是否已经被加载到DOM中。一旦条件满足，代码就会继续执行；如果在`WebDriverWait`指定的时间内条件没有满足，Selenium将抛出一个超时异常。

通过以上解释，您可以看出`input.send_keys(Keys.ENTER)`是如何触发页面的搜索功能，以及如何使用DOM和Selenium的等待机制来处理动态内容的加载。 """