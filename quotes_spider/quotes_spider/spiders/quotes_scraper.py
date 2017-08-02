# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from quotes_spider.items import QuoteItem, AuthorItem


class QuotesScraperSpider(CrawlSpider):
    name = 'quotes_scraper'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com//']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[contains(text(),"Next")]', deny=r'tag/'), callback='parse_quotes', follow=True),
        Rule(LinkExtractor(allow=r'author/'), callback='parse_author', follow=True)
    )

    def parse_quotes(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        quote_list = []
        for quote in quotes:
            i = QuoteItem()
            i['author'] = quote.css('small.author::text').extract_first()
            tags = quote.xpath('.//a[@class="tag"]/text()').extract()
            i['tags'] = ', '.join(tags)
            i['text'] = quote.xpath('.//span[@class="text"]/text()').extract_first()
            i['url'] = response.url
            quote_list.append(i)
        return quote_list

    def parse_author(self, response):
        """ This function parses a sample Author response. Some contracts are mingled
        with this docstring.

        @url http://quotes.toscrape.com/author/Albert-Einstein/
        @returns items 1
        @returns requests 0
        @scrapes name birth_date birth_location description url
        """
        i = AuthorItem()
        i['name'] = response.xpath('//h3[@class="author-title"]/text()').extract_first().strip()
        i['birth_date'] = response.xpath('//span[@class="author-born-date"]/text()').extract_first()
        birth_location = response.xpath('//span[@class="author-born-location"]/text()').extract_first()
        if birth_location:
            i['birth_location'] = birth_location.replace('in ', '')
        i['description'] = response.xpath('//div[@class="author-description"]/text()').extract_first().strip()
        i['url'] = response.url
        return i
