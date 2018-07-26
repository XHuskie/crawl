# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']

        if len(data_list) == 0:
            return

        for data in data_list:
            item = DouyuItem()
            item['nickname'] = data['nickname']
            item['imagelink'] = data['vertical_src']

            yield item

        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
