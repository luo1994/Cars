# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BrandScrapyItem(scrapy.Item):
    """定义需要格式化的内容（或是需要保存到数据库的字段）"""
    # define the fields for your item here like:
    brand_id = scrapy.Field()
    brand_name = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """insert into auto_home_brand (id, name) VALUES (%s, %s) """
        params = (self["brand_id"], self["brand_name"])
        return insert_sql, params

    def distinct_data(self):
        query = """select id from auto_home_brand where id =%s"""
        params = (self["brand_id"])
        return query, params
