# Python 第一个爬虫练习
爬取百度百科 python 词条 1000个

## 环境
python3

### 依赖
   urllib、bs4、re、html
### 运行
    python spider_main.py

如果爬取不了，则百度修改了页面，根据页面修改爬取规则（ html_parser.py 修改规则）

* spider_main 爬虫总调度程序
* url_manager url 管理器
* html_download html 下载器
* html_parser html 解析器
* html_output 输出
