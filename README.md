# spide 爬虫思路

## python爬取百度百科

### 从python总入口进去：
 1. 循环从url管理器中找是否含有url
 2. 下载器下载url，返回html
 3. 解析器解析html，返回urls和data
 4. url管理器装载urls（先判断是否含有url）
 5. 输出器输出数据到html中

 完毕。
