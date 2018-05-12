# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import os
import requests


class ScrapyjiandanPipeline(object):
    def process_item(self, item, spider):
        return item

class MeizituPipeline(object):
    def process_item(self, item, spider):
        if item.__class__.__name__ is 'MeizituItem':
            # url = item['url'].encode('utf8')
            url = item['url']
            imgName = url.split('/')[4]
            self.download_image(url, imgName)
        return item

    def download_image(self, url, name):
        if url == None or url == '':
            return None

        images_path = 'result/meizitu/'
        file_path = images_path + name
        file_name = name

        if os.path.exists(file_path):
            file_name = str(datetime.datetime.now()) + '_' + file_name
            file_path = images_path + file_name

        print(file_name)

        with open(file_path, 'wb') as handle:
            response = requests.get(url, stream=True)
            for block in response.iter_content(1024):
                if not block:
                    break
                
                handle.write(block)
        pass