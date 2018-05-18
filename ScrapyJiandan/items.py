# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyjiandanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MeizituItem(scrapy.Item):
    url = scrapy.Field()
    pass

class NewsItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    desc = scrapy.Field()
    detail_url = scrapy.Field()
    times = scrapy.Field()
    first_paragraph = scrapy.Field()
    pass
