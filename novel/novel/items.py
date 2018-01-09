# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小说名字
    name = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 小说类型
    novel_type = scrapy.Field()
    # 连载状态
    status = scrapy.Field()
    # 简介
    intro = scrapy.Field()
    # 更新状态
    update = scrapy.Field()
    # 更新时间
    update_time = scrapy.Field()
    # 小说页面
    novel_url = scrapy.Field()
