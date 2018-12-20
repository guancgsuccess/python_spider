# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
class B(ImagesPipeline):

    default_headers = {
        'accept': 'image/webp,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'referer': 'http://search.jumei.com',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }


    def get_media_requests(self, item, info):
        """
        :param item: 上一个管道中返回的item
        :param info:
        :return:
        """
        print('info------------',info)
        # referer = item['img_url']
        # self.default_headers['referer'] = referer
        yield Request(item['img_url'], headers=self.default_headers, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        """
        :param request: 每一个图片下载管道请求
        :param response:
        :param info:
        :param strip :清洗Windows系统的文件夹非法字符，避免无法创建目录
        :return: 每套图的分类目录
        """
        item = request.meta['item']
        print('item================================>',item)
        folder = item['title']
        # folder_strip = self.strip(folder)
        image_guid = request.url.split('/')[-1]
        filename = u'full/{0}/{1}'.format(folder, image_guid)
        return filename

    def item_completed(self, results, item, info):
        print('?????????????????????????result????????????')
        print('item-------------',item)
        print('info-------------',info)
        print('results',results)
        image_paths = [x['path'] for ok, x in results if ok]
        print('imge_paths==========>',image_paths)
        if not image_paths:
            raise DropItem("Item contains no images")
        return item