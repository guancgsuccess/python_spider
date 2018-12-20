# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class MyspidersPipeline(object):
    def process_item(self, item, spider):
        print('****pipeline***')
        print(item)
        return item
#
class TestPipeline(object):
    def process_item(self,item,spider):
        print('?????????test?????')
        print(item)
        return item

class JumeiSavePipeline(object):
    def __init__(self):
        self.fp = open('jumei.json', 'a+',encoding='utf-8')
        self.goods = []

    def process_item(self, item, spider):
        line = dict(item)
        self.goods.append(line)
        print('**********************')
        print(line)
        return item

    def close_spider(self, spider):
        # pass
        json.dump(self.goods, self.fp, ensure_ascii=False)
        self.fp.close()