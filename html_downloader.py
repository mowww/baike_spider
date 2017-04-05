# encoding = utf-8
from urllib import request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        re = request.urlopen(url)
        if re.getcode() != 200:
            return None
        return re.read()


