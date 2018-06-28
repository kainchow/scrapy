# -*- coding: utf-8 -*-
import scrapy
from tujia_city_id.items import TujiaCityIdItem
from tujia_city_id.settings import *
import json


class CityIdSpider(scrapy.Spider):
    name = 'city_id'
    allowed_domains = ['www.tujia.com']
    start_urls = ['https://www.tujia.com/api/pccity/cityinforguonei']

    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def  make_requests_from_url(self, url):
        return scrapy.Request(url, method='POST', headers=DEFAULT_REQUEST_HEADERS, dont_filter=True)
    
    def parse(self, response):
        result = json.loads(response.text)
        citys = result.get('citys')
        for city in citys:
            item = TujiaCityIdItem()
            item['_id'] = city.get('id')
            item['name'] = city.get('name')
            item['pinyin'] = city.get('pinyin')
            item['scenicspot'] = city.get('scenicspot')
            item['scenicspotId'] = city.get('scenicspotId')
            item['keyword'] = city.get('keyword')
            yield item

