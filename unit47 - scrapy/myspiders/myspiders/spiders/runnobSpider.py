# -*- coding: utf-8 -*-
import scrapy


class RunnobspiderSpider(scrapy.Spider):
    name = 'runnobSpider'
    allowed_domains = ['http://www.runoob.com']
    start_urls = ['http://www.runoob.com/']

    def parse(self, response):
        print(response.body)
        pass
