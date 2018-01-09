# -*- coding: utf-8 -*-
from novel.settings import *
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NovelPipeline(object):

    con = pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        db=MYSQL_DB,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        charset='utf8'
    )
    cur = con.cursor()
    create_sql = """CREATE TABLE novel(
                    `name` VARCHAR(255) NOT NULL, 
                    `author` VARCHAR(255) NOT NULL, 
                    `novel_type` VARCHAR(255) NOT NULL, 
                    `status` VARCHAR(255) NOT NULL, 
                    `intro` VARCHAR(255) NOT NULL, 
                    `update` VARCHAR(255) NOT NULL, 
                    `update_time` VARCHAR(255) NOT NULL,
                    `novel_url` VARCHAR(255) NOT NULL
                    );
                """
    try:
        cur.execute(create_sql)
    except pymysql.err.InternalError:
        pass

    def process_item(self, item, spider):
        insert_sql = """INSERT INTO novel(`name`, `author`, `novel_type`, `status`, `intro`, `update`, `update_time`, 
                        `novel_url`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                    """
        self.cur.execute(insert_sql, (item['name'], item['author'], item['novel_type'], item['status'], item['intro'],
                                      item['update'], item['update_time'], item['novel_url']))
        self.con.commit()
