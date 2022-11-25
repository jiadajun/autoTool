Playwright 是微软在 2020 年初开源的新一代自动化测试工具，它的功能类似于 Selenium、Pyppeteer 等，都可以驱动浏览器进行各种自动化操作。它的功能也非常强大，对市面上的主流浏览器都提供了支持，API 功能简洁又强大。虽然诞生比较晚，但是现在发展得非常火热。


 Playwright 的特点
Playwright 支持当前所有主流浏览器，包括 Chrome 和 Edge（基于 Chromium）、Firefox、Safari（基于 WebKit） ，提供完善的自动化控制的 API。

Playwright 支持移动端页面测试，使用设备模拟技术可以使我们在移动 Web 浏览器中测试响应式 Web 应用程序。

Playwright 支持所有浏览器的 Headless 模式和非 Headless 模式的测试。

Playwright 的安装和配置非常简单，安装过程中会自动安装对应的浏览器和驱动，不需要额外配置 WebDriver 等。

Playwright 提供了自动等待相关的 API，当页面加载的时候会自动等待对应的节点加载，大大简化了 API 编写复杂度。

安装
Playwright 目前提供了 Python 和 Node.js 的 API，下面我们针对 Python 版的 Playwright 进行介绍。

要使用 Playwright，需要 Python 3.7 版本及以上，请确保 Python 的版本符合要求。

要安装 Playwright，可以直接使用 pip3，命令如下：
pip3 install playwright


安装完成之后需要进行一些初始化操作：

playwright install


这时候 Playwrigth 会安装 Chromium, Firefox and WebKit 浏览器并配置一些驱动，我们不必关心中间配置的过程，Playwright 会为我们配置好。

基本使用

Playwright 支持两种编写模式，一种是类似 Pyppetter 一样的异步模式，另一种是像 Selenium 一样的同步模式，我们可以根据实际需要选择使用不同的模式。


首先我们导入了 sync_playwright 方法，然后直接调用了这个方法，该方法返回的是一个 PlaywrightContextManager 对象，可以理解是一个浏览器上下文管理器，我们将其赋值为变量 p。

接着我们调用了 PlaywrightContextManager 对象的 chromium、firefox、webkit 属性依次创建了一个 Chromium、Firefox 以及 Webkit 浏览器实例，接着用一个 for 循环依次执行了它们的 launch 方法，同时设置了 headless 参数为 False。


注意：如果不设置为 False，默认是无头模式启动浏览器，我们看不到任何窗口。


 代码生成
Playwright 还有一个强大的功能，那就是可以录制我们在浏览器中的操作并将代码自动生成出来，有了这个功能，我们甚至都不用写任何一行代码，这个功能可以通过 playwright 命令行调用 codegen 来实现，我们先来看看 codegen 命令都有什么参数，输入如下命令：


移动端浏览器支持

Playwright 另外一个特色功能就是可以支持移动端浏览器的模拟，比如模拟打开 iPhone 12 Pro Max 上的 Safari 浏览器，然后手动设置定位，并打开百度地图并截图。首先我们可以选定一个经纬度，比如故宫的经纬度是 39.913904, 116.39014，我们可以通过 geolocation 参数传递给 Webkit 浏览器并初始化。

