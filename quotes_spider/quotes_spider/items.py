# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuoteItem(scrapy.Item):
    author = scrapy.Field()
    tags = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()

class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    birth_date = scrapy.Field()
    birth_location = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
