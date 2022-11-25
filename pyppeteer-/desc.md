pyppeteer 是非官方 Python 版本的 Puppeteer 库，浏览器自动化库，由日本工程师开发。

Puppeteer 是 Google 基于 Node.js 开发的工具，调用 Chrome 的 API，通过 JavaScript 代码来操纵 Chrome 完成一些操作，用于网络爬虫、Web 程序自动测试等。


 
安装 pyppeteer
pip install pyppeteer
1
安装 Chromium
pyppeteer-install


查看 Chromium 存放路径
import pyppeteer

print(pyppeteer.__chromium_revision__)  # 查看版本号

print(pyppeteer.executablePath())  # 查看 Chromium 存放路径

588429
C:\Users\Administrator\AppData\Local\pyppeteer\pyppeteer\local-chromium\588429\chrome-win32\chrome.exe
链接：https://blog.csdn.net/lly1122334/article/details/107364106