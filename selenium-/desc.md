
1.配置基础环境 

文档 ： https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/install_drivers/

安装selenium库
pip install selenium

下载驱动

Firefox 浏览器驱动 https://github.com/mozilla/geckodriver/releases

IE 浏览器驱动 http://selenium-release.storage.googleapis.com/index.html

Edge 浏览器驱动 https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

PhantomJS 浏览器驱动 https://phantomjs.org/

Opera 浏览器驱动  https://github.com/operasoftware/operachromiumdriver/releases

chromedriver 版 https://chromedriver.storage.googleapis.com/index.html


 我的版本（版本 107.0.5304.107（正式版本） （64 位））
在该网站找到匹配自己chromium浏览器版本的压缩包，前面三段版本号匹配就可

将 chromedriver.exe 保存到任意位置，并把当前路径保存到环境变量中（我的电脑>>右键属性>>高级系统设置>>高级>>环境变量>>系统变量>>Path），添加的时候要注意不要把 path 变量给覆盖了，如果覆盖了千万别关机，然后百度。添加成功后使用下面代码进行测试。

PATH :

C:\Program Files\Google\Chrome\Application

D:\kanxue\ie_driver\chromedriver_win32\chromedriver.exe

注意文件名不要和包名字冲突