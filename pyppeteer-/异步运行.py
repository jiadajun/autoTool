import asyncio
from pyppeteer import launch


async def crawl(url):
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto(url)
    title = await page.title()
    print(title)
    await browser.close()


async def main():
    urls = [
        crawl('https://www.baidu.com/'),
        crawl('https://www.bing.com/')
    ]
    await asyncio.wait(urls)
    # await asyncio.gather(*urls)


asyncio.get_event_loop().run_until_complete(main())
# 百度一下，你就知道
# 微软 Bing 搜索 - 国内版
