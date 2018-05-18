# -*- coding: utf-8 -*-
import scrapy, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ScrapyJiandan.items import MeizituItem


class MeizituListSpider(scrapy.Spider):
    name = "meizituList"
    allowed_domains = ["jandan.net/ooxx"]
    start_urls = ['http://jandan.net/ooxx/']
    start_url_selenium = 'http://jandan.net/ooxx/'
    maxPage = 1

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        pass
        
    def parse(self, response):
        self.driver.get(self.start_url_selenium)

        pageurl = self.driver.find_element_by_css_selector('#comments > div:nth-child(6) > div > a.previous-comment-page')

        print('next_page---%s' % pageurl.get_attribute('href'))

        item = MeizituItem()

        # click loading more
        for i in range(self.maxPage):

            yield from self.parse_detail(item)

            print('===click loading==')
            self.driver.execute_script('\
              document.querySelector("#comments > div:nth-child(6) > div > a.previous-comment-page")\
              &&document.querySelector("#comments > div:nth-child(6) > div > a.previous-comment-page").click()\
            ')
            print('==============================')
        
            pageurl = self.driver.find_element_by_css_selector('#comments > div:nth-child(6) > div > a.previous-comment-page')

            print('next_page--%s' % pageurl.get_attribute('href'), i)
            # time.sleep(i*2)
            time.sleep(3)

        self.driver.close()
        pass

    def parse_detail(self, item):
        liEles = self.driver.find_elements_by_css_selector('#comments > ol > li')
        for li in liEles:
            try:
                img = li.find_element_by_css_selector('div > div > div.text > p > img')

                if img is None:
                    continue
                print('=============')
                src = img.get_attribute('src')
                print(src)
                print('=============')
                item['url'] = src
                yield item
            except:
                continue
        pass
