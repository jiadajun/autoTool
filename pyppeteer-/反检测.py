import asyncio
from pyppeteer import launch


async def main():
    # browser = await launch(executablePath='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless=False)
    browser = await launch(headless=False)

    page = await browser.newPage()
    await page.evaluateOnNewDocument('''() => {
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
        }
    ''')
    await page.goto('https://www.baidu.com/')
    input('检查完毕后按下回车键关闭窗口...')
    await browser.close()


asyncio.run(main())