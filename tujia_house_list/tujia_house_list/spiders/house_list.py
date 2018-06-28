# -*- coding: utf-8 -*-
from json import JSONDecodeError

from scrapy import Spider, Request
from scrapy.http import FormRequest
import json
from tujia_house_list.items import HouseListItem
from tujia_house_list.settings import FORM_DATA


class HouseListSpider(Spider):
    name = 'house_list'
    allowed_domains = ['www.tujia.com']
    start_urls = ['https://www.tujia.com/bingo/pc/search/searchUnit']

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url, method='POST', body=json.dumps(FORM_DATA), callback=self.parse)

    def parse(self, response):
        try:
            units = json.loads(response.text).get('data').get('units')
            for unit in units:
                item = HouseListItem()
                for field in item.fields:
                    item[field] = unit.get(field)
                yield item
        except AttributeError:
            pass
        
        all_page = round(json.loads(response.text).get('data').get('totalUnitCount') / 30)
        for page in range(2, all_page + 1):
            FORM_DATA['pageIndex'] = page
            yield Request(self.start_urls[0], method='POST', body=json.dumps(FORM_DATA),callback=self.parse)

