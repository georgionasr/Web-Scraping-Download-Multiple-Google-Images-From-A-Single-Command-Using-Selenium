# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request



class GoogleImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        return [Request(x, meta={'image_name':item.get('image_name')}) for x in item.get(self.images_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        filename = request.meta['image_name'].replace(':',' ')
        filename = filename.replace('<',' ')
        filename = filename.replace('>',' ')
        filename = filename.replace('"',' ')
        filename = filename.replace('/',' ')
        filename = filename.replace('\\',' ')
        filename = filename.replace('|',' ')
        filename = filename.replace('?',' ')
        filename = filename.replace('*',' ')
        return 'downloads/%s.jpg' % (filename)
