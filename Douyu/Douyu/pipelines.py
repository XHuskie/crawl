# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from Douyu.settings import IMAGES_STORE as images_store


class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link = item['imagelink']
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results]
        os.rename(images_store + image_path[0], images_store + item['nickname'] + ".jpg")
        return item
