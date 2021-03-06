# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo

from scrapy.conf import settings
from items import ZhihuItem
from scrapy import log


class ZhihuPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise ZhihuItem("Missing {0}!".format(data))
        else:
            if not self.collection.find({'url': item['url']}).count():
                self.collection.insert(dict(item))
                log.msg("Question added to MongoDB database!",
                        level=log.DEBUG, spider=spider)
            else:
                self.collection.update({'url': item['url']}, dict(item))
                log.msg("Question update to MongoDB database!",
                        level=log.DEBUG, spider=spider)
        return item
