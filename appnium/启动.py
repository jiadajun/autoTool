from appium import webdriver  # 后续操作依赖于这个库
from selenium.webdriver.common.by import By

desired_caps = {
    'platformName': 'Android',  # 设备类型；
    'platformVersion': '9',  # 设备的类型的版本号，如果是安卓，填写大的版本号即可，小数不用填；
    'deviceName': 'MI9',  # 设备的名称，这个和后续的测试没有多大关系；
    'appPackage': 'com.shuqi.controller',  # 需要测试的app包名；
    'appActivity': 'com.shuqi.activity.SplashActivity',  # 需要测试的app启动名；
    # 'unicodeKeyboard': True,  # 如果指定了UI2作为驱动，不需要配置；
    # 'resetKeyboard': True,  # 重置自动化时设置的键盘；
    'chromedriverExecutableDir': 'D:\kanxue\ie_driver\chromedriver_win32\chromedriver.exe',  # 启动webview的webdriver驱动
    'noReset': True,  # 防止每次启动app时候都初始化所有数据；
    'newCommandTimeout': 6000,  # 代码向appiumserver发送命令的延迟时间，单位是秒，不设置默认一分钟；
    'automationName': 'uiautomator2',  # 这个并不是所有应用都适配的，1.15.1以前默认是UI1，之后是默认UI2；
#     'autoGrantPermissions': True,  # 自动跳过授权
#     'skipServerInstallation': True,
#     'skipDeviceInitialization': True,  # 跳过安装AppiumSetting
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # /wd/hub 路径是固定的，desired_caps是初始化设置的字典；
driver.implicitly_wait(10)  # 隐式等待和selenium的用法是一样的；

driver.find_element(By.ID,"com.shuqi.controller:id/pager_tabbar_text").click()

driver.implicitly_wait(3)  # 隐式等待和selenium的用法是一样的；

driver.find_element(By.ID,"com.shuqi.controller:id/iv_tab_root_bg").click()
