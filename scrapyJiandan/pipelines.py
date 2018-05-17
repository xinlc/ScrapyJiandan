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
        if url is None or url == '':
            return None

        images_path = 'result/meizitu/'

        if not os.path.exists(images_path):
            os.makedirs(images_path)

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


class NewsPipeline(object):
    def process_item(self, item, spider):
        if item.__class__.__name__ is 'NewsItem':

            file_path = 'result/news/'

            if not os.path.exists(file_path):
                os.makedirs(file_path)

            with open(file_path + str(datetime.datetime.now().strftime('%Y-%m-%d-%H')) + '.csv',
                      'a') as f:

                # plaintext = item['title'].encode('utf8') + ','\
                #         + item['author'].encode('utf8') + ','\
                #         + (item['tag'].encode('utf8') if 'tag' in item else 'N/A') + ','\
                #         + (item['desc'].encode('utf8') if 'desc' in item else 'N/A') + ','\
                #         + (item['times'].encode('utf8') if 'times' in item else 'N/A') + ','\
                #         + (item['first_paragraph'].encode('utf8') if 'first_paragraph' in item else 'N/A') + ','\
                #         + (item['detail_url'].encode('utf8') if 'detail_url' in item else 'N/A') + ','\
                #         + '\n'

                plaintext = item['title'] + ','\
                        + item['author'] + ','\
                        + (item['tag'] if 'tag' in item else 'N/A') + ','\
                        + (item['desc'] if 'desc' in item else 'N/A') + ','\
                        + (item['times'] if 'times' in item else 'N/A') + ','\
                        + (item['first_paragraph'] if 'first_paragraph' in item else 'N/A') + ','\
                        + (item['detail_url'] if 'detail_url' in item else 'N/A') + ','\
                        + '\n'

                f.write(plaintext)
        return item


