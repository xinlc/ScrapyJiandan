# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ScrapyJiandan.items import MeizituItem


class MeizituSpider(scrapy.Spider):
    name = "meizitu"
    allowed_domains = ["jandan.net/ooxx"]
    start_urls = ['http://jandan.net/ooxx/']
    start_url_selenium = 'http://jandan.net/ooxx/'

    def __init__(self):

        # [Download PhantomJS](http://phantomjs.org/download.html)
        # self.driver = webdriver.PhantomJS(executable_path="/Users/leo/Documents/phantomjs-2.1.1-macosx/bin/phantomjs")
        # Selenium support for PhantomJS has been deprecated, please use headless
        # self.driver = webdriver.Chrome(executable_path="/Users/leo/Documents/chromedriver")

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        pass
        
    def parse(self, response):
        item = MeizituItem()
        self.driver.get(self.start_url_selenium)
        liEles = self.driver.find_elements_by_css_selector('#comments > ol > li')

        for li in liEles:

            try:
                img = li.find_element_by_css_selector('div > div > div.text > p > img')

                if img == None:
                    continue
                print ('-------------')
                src = img.get_attribute('src')
                print (src)
                print ('=============')
                item['url'] = src
                yield item
            except:
                continue

        self.driver.close()
        pass

    # def parse(self, response):
    #     item = MeizituItem()
    #     liEles = response.css('#comments > ol > li')

    #     for li in liEles:
    #         item['url'] = li.css('div > div > div.text > p > img::attr(src)').extract_first()
    #         print(item['url'])
    #     yield item
    #     pass
