"""
反检测的演示:
    具体的网站还是要根据具体的实现
"""

from selenium.webdriver import Chrome
# 导入反检测使用的
from selenium.webdriver import ChromeOptions

if __name__ == '__main__':
    # 创建选项对象
    options_ = ChromeOptions()
    # 添加参数,进行隐藏
    options_.add_experimental_option('excludeSwitches', ["enable-automation"])  # 不需要死记硬背

    chrome_obj = Chrome(options=options_)

    chrome_obj.get('https://www.baidu.com')

    chrome_obj.quit()