from selenium import webdriver
from selenium.webdriver.common.by import By

#初始化驱动
driver = webdriver.Chrome()
#打开页面
driver.get("https://www.google.com")
#获取页面标题
driver.title # => "Google"
#隐式等待 会在指定的时间范围内不断的查找元素，直到找到元素或超时，特点是必须等待整个页面加载完成。
driver.implicitly_wait(0.5)
#通过name定位输入框元素
search_box = driver.find_element(By.NAME, "q")
#通过name定位点击按钮
search_button = driver.find_element(By.NAME, "btnK")
#向输入框填文字
search_box.send_keys("Selenium")
#点击添加按钮
search_button.click()
#获取输入框内容
driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"
#退出控制
driver.quit()

