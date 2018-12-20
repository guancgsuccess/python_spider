# -*- coding: utf-8 -*-
import scrapy
from myspiders.items import RunnoobItem

class RunnobspiderSpider(scrapy.Spider):
    name = 'runnobSpider'
    allowed_domains = ['runoob.com']
    start_urls = ['http://www.runoob.com/']

    def parse(self, response):
        #print(response.body)
        #pass

        # 解析找到导航
        #links = response.xpath('//div[@class="col nav"]/ul/li')
        links = response.css('div[class="col nav"] ul li')
        items = []
        for link in links:
            item = RunnoobItem()
            item['href'] = link.xpath('a/@href').extract()
            item['title'] = link.xpath('a/text()').extract()

            yield item
            #items.append(item)
        #return items