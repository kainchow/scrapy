# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from novel.items import NovelItem


class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['readnovel.com']
    start_urls = ['https://www.readnovel.com/rank/xyyuepiao?pageNum=1']
    url_page = 'https://www.readnovel.com/rank/xyyuepiao?pageNum='
    url_bash = 'https://www.readnovel.com'
    page = 2

    def parse(self, response):
        books = response.xpath('//div[@class="book-img-text"]/ul/li')
        for book in books:
            item = NovelItem()
            item['name'] = book.xpath('./div[2]/h4/a/text()').extract()[0]
            item['author'] = book.xpath('./div[2]/p[1]/a[1]/text()').extract()[0]
            item['novel_type'] = book.xpath('./div[2]/p[1]/a[2]/text()').extract()[0]
            item['status'] = book.xpath('./div[2]/p[1]/span/text()').extract()[0]
            item['intro'] = book.xpath('./div[2]/p[2]/text()').extract()[0].strip()
            item['update'] = book.xpath('./div[2]/p[3]/a/text()').extract()[0]
            item['update_time'] = book.xpath('./div[2]/p[3]/span/text()').extract()[0]
            item['novel_url'] = self.url_bash + book.xpath('./div[2]/h4/a/@href').extract()[0]
            yield item

        next_page = response.xpath('//div[@class="page-box cf"]/div/@data-pagemax').extract()[0]
        if self.page <= int(next_page):
            yield Request(url=self.url_page + str(self.page), callback=self.parse)
            self.page += 1
