Firefox插件FoxyProxy辅助添加白名单。此工具的出现主要为了解决在使用burp抓包的过程中会将所有请求包全部抓取，有时候我们并不想抓取所有请求包。那么配合firefox的插件FoxyProxy即可实现只抓取想要的域名，完美的解决了此问题。感谢手动@joner11234师傅帮忙完成Orz

用法：

将要添加白名单域名放到domain.txt，运行脚本会生成new_file.json

Python3 firefox-proxy.py

打开插件模式页面选择new_file.json导入
<img width="1137" alt="图片" src="https://user-images.githubusercontent.com/71672296/205484778-f9325fdd-28a7-4c0f-bf5c-e6d8a589fda5.png">
