# -*- coding: utf-8 -*-
import scrapy


class RunnobspiderSpider(scrapy.Spider):
    name = 'runnobSpider'
    allowed_domains = ['http://www.runoob.com']
    start_urls = ['http://http://www.runoob.com/']

    def parse(self, response):
        pass
