# encoding = utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_url(self, url):
        if url is None:
            return
        self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        newurl = self.new_urls.pop()
        self.old_urls.add(newurl)
        return newurl

    def add_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for x in new_urls:
            self.add_url(x)

