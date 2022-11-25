Airtest是由网易游戏推出的UI自动化测试解决方案，是一个跨平台的、 基于图像识别 的UI自动化测试框架，适用于游戏和App，支持平台有Windows、Android和iOS。并且提供了基于UI控件识别的Poco框架，目前也支持Android原生、iOS原生、Unity3D、cocos2dx、UE4和Egret等平台。为了让测试人员更好上手，网易还贴心地提供了AirtestIDE工具，内置了Airtest和Poco的相关插件功能，能够使用它快速简单地编写 Airtest 和 Poco 代码。
如果你是一个自动化新手同学，建议借助AirtestIDE编写/运行自动化脚本；但是当你能够熟练使用Airtest和Poco框架之后，那就使用python语言自由发会编写自动化脚本吧



```angular2html
1.各种官方教程文档：
1）官方教程文档：https://airtest.doc.io.netease.com/

2）Airtest API文档：https://airtest.readthedocs.io/zh_CN/latest/

3）poco API文档：https://poco.readthedocs.io/zh_CN/latest/index.html

4）Airtest官方博客：https://juejin.im/user/1275089221067928

2.各种官网地址：
1）AirtestProject项目官网：http://airtest.netease.com/

2）AirtestIDE下载官网：http://airtest.netease.com/changelog.html

3）Airtest开源地址：https://github.com/AirtestProject/Airtest

4）poco开源地址：https://github.com/AirtestProject/Poco/

5）企业级自动化解决方案-私有云：https://airlab.163.com/b2b

3.与官方交流
1）官方公众号：AirtestProject

2）官方答疑Q群：1群437119175（已满）、2群1017250147（仅剩少量名额）

4.常见api的详细介绍
1）touch点击： https://mp.weixin.qq.com/s/rrAgQCjGKZs2pzgzG496HA

2）swipe滑动：https://mp.weixin.qq.com/s/EjVDlRtM99EW_Uw7M0dQ-Q

3）text输入： https://mp.weixin.qq.com/s/WyqNa9-riLIpzEBEemT2GQ

4）keyevent大全：https://mp.weixin.qq.com/s/HXZVd1uwaOd9gt7IVBGNDQ

5）Assert断言： https://mp.weixin.qq.com/s/DEe-Emyi0hN0JZA83i1Wmg

5.测试框架教程
1）poco的元素定位： https://mp.weixin.qq.com/s/PYI-kGWZCpoaxe2Tmw5d5Q

2）poco常用api介绍： https://mp.weixin.qq.com/s/PonBynNPfLqaWzp2oc689Q

3）在IDE中使用airtest-selenium：https://mp.weixin.qq.com/s/Fw5O8dXQ3bAX8UoyWuW9Lw

4）selenium常用api介绍：https://mp.weixin.qq.com/s/USSITxVH9ebueyIfSPhbSw

6.基础知识教程 坐标相关
1）Airtest和poco的坐标系介绍（绝对坐标与相对坐标）：https://mp.weixin.qq.com/s/6yu0gjCEZQ_x6NwEY_rBjQ

截图相关
2）截图识别失败、提高截图脚本兼容性01：https://mp.weixin.qq.com/s/M5RXb9Gts_nMGHODovjQew

3）截图识别失败、提高截图脚本兼容性02：https://mp.weixin.qq.com/s/lOK5lrBlmd6CGAleCZ1KwA

4）Airtest的截图识别算法介绍：https://mp.weixin.qq.com/s/cGFvU9C7mBpsmnWgDLPW5A

报告相关
5）生成、导出报告全攻略：https://mp.weixin.qq.com/s/NDCcs4egVFe4Bngg_qjfjA

6）用脚本实现自动发送测试报告到指定邮箱：https://mp.weixin.qq.com/s/a23cKOBYU9jOcw6VSEcBRg

7）用命令行生成、导出报告：https://mp.weixin.qq.com/s/bc-xcCmbgHLKP9cMdhS97g

iOS自动化
8）iOS应用自动化实操： https://mp.weixin.qq.com/s/XEqsOxIhXGjpGhUzCe4RXw

9）模拟清除iOS后台应用：https://mp.weixin.qq.com/s/wfXATdx_U5gpwIQcSQHe2g

Windows自动化
10）Windows自动化实操： https://mp.weixin.qq.com/s/SaBCwYHTF8mnNLjBlnzt7w

11）IDE连接Windows窗口相关问题：https://mp.weixin.qq.com/s/sFdxHOXt9nIM326pnK0UGw

设备连接相关
12）各种连接设备的接口介绍：https://mp.weixin.qq.com/s/znYi-eCifeMXfce9GDpW-w

13）连接安卓模拟器的常见问题：https://mp.weixin.qq.com/s/us4Jr9t21nNyKs-bGD9yyg

14）连接模拟器的案例实操：https://mp.weixin.qq.com/s/2_K4AKCfHQ59wgedXZ23wA

安卓微信小程序
15）测试安卓的微信小程序：https://mp.weixin.qq.com/s/R02Ac3ZC1B_ND7QVik_Z8Q

7.常见问题及解决办法
1）录制脚本运行的视频： https://mp.weixin.qq.com/s/3JsVjwikjo4OmtcjvmktRw

2）Yosemite输入法的相关问题：https://mp.weixin.qq.com/s/LnzToiXFVcfkeOGz8Vz9Pw

3）IDE的安卓小助手： https://mp.weixin.qq.com/s/EH0aQnr2AwG0MmFdgoE7mw

4）模拟滑动解锁、多指滑动等：https://mp.weixin.qq.com/s/JiIT0CkiY7zcdqUo-AI0GQ

5）局部截图和局部找图功能：https://mp.weixin.qq.com/s/Kd_EQit9UG5CLxw-EHM1Uw

6）.air脚本和.py脚本的区别：https://mp.weixin.qq.com/s/-gGplycWKAsJ6Os3XQFARA

7）用pycharm编写airtest脚本的常见问题：https://mp.weixin.qq.com/s/Ha2Oq02lkDmMokwPxFpN6A

8）选择poco模式之后查看不到UI树：
https://airtest.doc.io.netease.com/IDEdocs/poco_framework/poco_quick_start/#pocoui

9）删除输入框的内容：
https://airtest.doc.io.netease.com/IDEdocs/faq/3_api_faq/#5

10）安卓设备连接问题：
https://airtest.doc.io.netease.com/IDEdocs/device_connection/2_android_faq/

11）最常问的8大问题01期：https://mp.weixin.qq.com/s/Z2K1a1UyKUhjqVnhMCN0CQ

12）最常问的8大问题02期：https://mp.weixin.qq.com/s/hUTNdeHuCre52DUUrQbJsQ

13）最常问的8大问题03期：https://mp.weixin.qq.com/s/YcSBMA_7tkImoEYCK7UyUQ

14）最常问的8大问题04期：https://mp.weixin.qq.com/s/sbrnP9ZT9aXBdM37K5M9LA

8.高级教程
1）自动化测试的文字识别：https://mp.weixin.qq.com/s/mrx2fndE9t_477yViZrpRA

2）Airtest脚本的批量运行：https://mp.weixin.qq.com/s/1YlUuiQCmMGb5_64S-si3Q

3）多机协作的实操案例： https://mp.weixin.qq.com/s/8q9IoFYvhGe1v6ow74Bfmg

4）从0到1打包项目并接入pocosdk：https://mp.weixin.qq.com/s/hhukqYAfjQ_dsQ06KC3A0g

5）提高遍历pocoUI树的效率：https://mp.weixin.qq.com/s/O5ckgX_cvOp6RQqSwYaxKg

6）如何修改Airtest源码：https://mp.weixin.qq.com/s/PnZBFrFW8f_Bn6v228fVSQ

9.自动化测试案例（含脚本）
1）APP登录和退出的自动化：https://mp.weixin.qq.com/s/7HkMHbk2CgNo_PKtB-MmKg

2）循环执行脚本的实操案例：https://mp.weixin.qq.com/s/u8HikcgDDrvPrAbiDwA7ZQ

3）调用其它脚本的实操案例：https://mp.weixin.qq.com/s/4RsrAhEutK7MOqVqWr_iyQ

4）用Airtest做爬虫的实操案例：https://mp.weixin.qq.com/s/-Agd4uC2irXwDTf77arSDA
```

Airtest是一个跨平台的UI自动化测试框架，适用于游戏和App。

如果你是Airtest新手用户，从 官网 开始上手吧。

以下文档会介绍Airtest的基本用法，以及提供API文档





