# -*- coding: utf-8 -*-
import scrapy
import bs4

class ErtSpider(scrapy.Spider):
    name = 'ert'
    allowed_domains = ['www.shuku.net']
    start_urls = ['http://www.shuku.net/novels/mulu/ert.html']

    def parse(self, response):
        all_html = response.text
        comment_catalog_start = u'<!-- 书目开始 -->'
        comment_catalog_end = u'<!-- 书目结束 -->'
        catalogs = all_html[all_html.index(comment_catalog_start) : all_html.index(comment_catalog_end)]

        soup = bs4.BeautifulSoup(catalogs, 'html.parser')

        for td in soup.find_all('td', class_='p9'):
            for c in td.contents:
                if isinstance(c, bs4.element.Tag):
                    next_page = c['href']
                    yield response.follow(next_page, self.parse_book_toc_page)

    def parse_book_toc_page(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        book_content_links = []
        for link in soup.find_all('a'):
            if 'target' not in link.attrs and 'http' not in link.attrs['href']:
                next_page = link['href']
                book_content_links.append(next_page)

        if len(book_content_links) == 0:
            yield self.parse_book_content(response)
        else:
            for next_page in book_content_links:
                yield response.follow(next_page, self.parse_book_content_page)
        
    def parse_book_content_page(self, response):
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        pre_tags = soup.find_all('pre')

        if len(pre_tags) == 1:
            pre_tag = soup.find('pre')
            content = pre_tag.contents[0]
            yield {
                'content': content
            }
