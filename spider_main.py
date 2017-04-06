# encoding = utf-8
from baike_python import html_downloader, html_output, html_parser, url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.down = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    def craw(self, url):
        self.urls.add_url(url)
        count = 0
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.down.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_urls(new_urls)
                self.output.collect_data(new_data)
                count += 1
                if count > 1000:
                    break
                print('craw %d: %s' % (count, new_url))
            except:
                print('craw failed %d' % count)
        self.output.output_html()
if __name__ == '__main__':
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

