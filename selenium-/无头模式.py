from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 实例化Options
opts = Options()
# 设置无头模式 相当于 opts.add_argument('--haedless')
opts.headless = True
# 设置options
dr = webdriver.Chrome(options=opts)
# 最大化窗口
dr.maximize_window
# 隐式等待8秒
dr.implicitly_wait(8)
#打开页面
dr.get("https://www.google.com")
#获取页面标题
dr.title # => "Google"
#隐式等待 会在指定的时间范围内不断的查找元素，直到找到元素或超时，特点是必须等待整个页面加载完成。
dr.implicitly_wait(0.5)
#通过name定位输入框元素
search_box = dr.find_element(By.NAME, "q")
#通过name定位点击按钮
search_button = dr.find_element(By.NAME, "btnK")
#向输入框填文字
search_box.send_keys("Selenium")
#点击添加按钮
search_button.click()
#获取输入框内容
dr.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"
# 截图可见
dr.save_screenshot(r'D:\woker\python\autoTool\selenium-\1.png')
dr.quit()