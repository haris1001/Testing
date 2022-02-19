# -*- coding: utf-8 -*-
import scrapy


class CodeSpider(scrapy.Spider):
    name = 'code'
    allowed_domains = ['code.com']
    start_urls = ['https://my.gumtree.com/postad/d5944aa8d8a44787b2fc9b21ac57e732']

    def parse(self, response):
        pass
