# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    url = scrapy.Field()
    question = scrapy.Field()
    follow_count = scrapy.Field()
    answer_count = scrapy.Field()
    created = scrapy.Field()
