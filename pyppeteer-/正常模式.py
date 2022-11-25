import asyncio
import pyppeteer
from pyppeteer import launch

print(pyppeteer.__chromium_revision__)  # 查看版本号
print(pyppeteer.executablePath())  # 查看 Chromium 存放路径
async def main():

    browser = await launch(headless=False)  # 关闭无头浏览器
    page = await browser.newPage()
    await page.goto('https://www.baidu.com/')  # 跳转
    await page.screenshot({'path': 'example.png'})  # 截图
    await browser.close()  # 关闭


asyncio.get_event_loop().run_until_complete(main())
