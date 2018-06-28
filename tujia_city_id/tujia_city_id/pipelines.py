# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MySQLPipeline(object):

    def __init__(self, mysql_user, mysql_pwd, mysql_db):
        self.mysql_user = mysql_user
        self.mysql_pwd = mysql_pwd
        self.mysql_db=mysql_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
                mysql_user = crawler.settings.get('MYSQL_USER'),
                mysql_pwd = crawler.settings.get('MYSQL_PASSWORD'),
                mysql_db = crawler.settings.get('MYSQL_DB')
                )

    def open_spider(self, spider):
        self.con = pymysql.connect(user=self.mysql_user, password=self.mysql_pwd, db=self.mysql_db, charset='utf8')
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        self.cur.execute("""insert into tujia_city_id (`_id`, `name`, `pinyin`, `scenicspot`, 
                `scenicspotId`, `keyword`) values (%s, %s, %s, %s, %s, %s)""",(item['_id'], item['name'], 
                    item['pinyin'], item['scenicspot'], item['scenicspotId'], item['keyword']))
        self.con.commit()
        return item

    def close_spider(self, spider):
        self.con.close()
