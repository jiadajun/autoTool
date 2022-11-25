CEF全称Chromium Embedded Framework，是一个基于Google Chromium 的开源项目。Google Chromium项目主要是为Google Chrome应用开发的，而CEF的目标则是为第三方应用提供可嵌入浏览器支持。CEF作用是在客户端嵌入网页界面。

嵌入一个兼容HTML5的浏览器控件到一个已经存在的本地应用。
创建一个轻量化的壳浏览器，用以托管主要用Web技术开发的应用。
有些应用有独立的绘制框架，使用CEF对Web内容做离线渲染。
使用CEF做自动化Web测试。



CEF3是多进程架构的，CEF3进程主要有一个Browser（浏览器）进程和多个Renderer（渲染）进程。Browser被定义为主进程，负责窗口管理，网络请求，网页管理 、网络交互。browser从服务器器请求到了响应，将html文本发送给Renderer 进程，render进程加载html，进行渲染，展示网页的内容；除此之外，Renderer进程还负责Js Binding和对Dom节点的访问。Browser和Renderer进程可以通过发送异步消息进行双向通信。



brower的创建：初始化创建、开启、消息循环、结束进程

安装： 

 pip install cefpython3


