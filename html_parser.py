# encoding = utf-8
from bs4 import BeautifulSoup
from urllib import parse
import re


class HtmlParser(object):
    def _get_new_urls(self, page_url, data, soup):
        res_urls = set()
        node = soup.find_all('a', href=re.compile(r'/item/\w+[/|\d+|%]+'))
        for n in node:
            res_url = parse.urljoin(page_url, n['href'])
            res_urls.add(res_url)
        return res_urls

    def _get_new_data(self, page_url, data, soup):
        # < dd class ="lemmaWgt-lemmaTitle-title" > <h1>Python</h1></dd>
        # url
        res_data = {}
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title")
        # 如果没找到 'lemmaWgt-lemmaTitle-title' 类，直接跳过
        if title_node is None:
            res_data['title'] = ''
            res_data['summary'] = ''
            return res_data
        else:
            title_node = title_node.find("h1")
            res_data['title'] = title_node.get_text()

        # <div class="lemma-summary">
        summary_node = soup.find('div', class_="lemma-summary")
        if summary_node is None:
            res_data['summary'] = ''
        else:
            res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, data):
        if page_url is None or data is None:
            return None
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, data, soup)
        new_data = self._get_new_data(page_url, data, soup)
        return new_urls, new_data



