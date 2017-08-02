# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from quotes_spider.items import QuoteItem, AuthorItem
import pymongo
import logging.handlers
from quotes_spider.settings import *
from scrapy.exceptions import DropItem

FORMAT='%(asctime)s [%(name)s] - %(message)s'
logger=logging.getLogger(__name__)
fh=logging.handlers.RotatingFileHandler("quotes_pipeline.log")
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(fh)

class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            MONGODB_SERVER,
            MONGODB_PORT
        )
        db = connection[MONGODB_DB]
        self.collection_q = db[MONGODB_COLLECTION_q]
        self.collection_a = db[MONGODB_COLLECTION_a]

    def process_item(self, item, spider):
        if isinstance(item, QuoteItem):
            return self.process_quote(item, spider)
        elif isinstance(item, AuthorItem):
            return self.process_author(item, spider)
        else:
            return item

    def process_quote(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection_q.insert(dict(item))
            logger.debug("Quote added to MongoDB database!")
        return item

    def process_author(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection_a.insert(dict(item))
            logger.debug("Author added to MongoDB database!")
        return item