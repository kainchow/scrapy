# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TujiaCityIdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    name = scrapy.Field()
    pinyin = scrapy.Field()
    scenicspot = scrapy.Field()
    scenicspotId = scrapy.Field()
    keyword = scrapy.Field()
