# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    # 公司
    company = scrapy.Field()
    # 薪水
    salary = scrapy.Field()
    # 经验
    experience = scrapy.Field()
    # 地址
    localhost = scrapy.Field()
    # 学历
    education = scrapy.Field()
