# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class LagouPipeline(object):
    def open_spider(self, spider):
        self.file = open('lagou.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        python_dict = dict(item)
        content = json.dumps(python_dict, ensure_ascii=False) + '\n'
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()
