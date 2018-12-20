# -*- coding: utf-8 -*-
import scrapy
import string
from urllib import parse
from myspiders.items import JumeiItem

class JumeispiderSpider(scrapy.Spider):
    name = 'jumeiSpider'
    #allowed_domains = ['jumei.com']
    #start_urls = ['http://jumei.com/']
    start_urls = []

    def start_requests(self):
        # http://search.jumei.com/?filter=0-11-1&search=%E9%9B%85%E8%AF%97%E5%85%B0%E9%BB%9B&from=&cat=

        # 查詢
        queryString = {
            "filter":"0-11-1",
            "search":"雅诗兰黛"
        }

        for i in range(1,2):
            # 构建url
            url = 'http://search.jumei.com/?'
            queryString['filter'] = '0-11-{0}'.format(i)
            url = url + parse.urlencode(queryString)

            url = parse.quote(url, safe=string.printable)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        nodes = response.xpath('//div[@class="products_wrap"]/ul/li')

        goods = []

        for node in nodes:
            good = JumeiItem()
            good['title']=node.xpath('.//div[@class="s_l_name"]/a/text()').re(r'\w{3,}')
            good['title'] = ''.join(good['title'])

            good['price'] = node.xpath('.//div[@class="search_list_price"]/span/text()').extract()[0]
            good['img_url'] = node.xpath('.//div[@class="s_l_pic"]/a/img/@src').extract()[0]
            #goods.append(good)
            yield good
        #print(goods)
        #pass
