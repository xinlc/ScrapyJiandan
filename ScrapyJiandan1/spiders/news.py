# -*- coding: utf-8 -*-
import scrapy, time
from ScrapyJiandan.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["jandan.net"]
    start_urls = ['http://jandan.net']
    maxPage = 2

    def __init__(self):
        pass

    def parse(self, response):
        list = response.css('#content > div.list-post')

        for post in list:
            item = NewsItem()

            # phone .re('1[3|4|5|7|8][0-9][\d,\s]+')
            # item['title'] = post.css('div.indexs > h2 > a::text').extract()[0]
            item['title'] = post.xpath('div[2]/h2/a/text()').extract()[0]
            detail_url = post.css('div.indexs > h2 > a::attr(href)').extract_first()
            item['author'] = post.css('div.indexs > div > a::text').extract_first()
            item['tag'] = post.css('div.indexs > div > strong > a::text').extract_first()
            # item['desc'] = post.xpath('div[2]/text()').extract()[0].strip()
            item['desc'] = post.xpath('div[2]/text()').re('[^\t,^\r,^\n]+')[0]
            item['detail_url'] = detail_url

            # print(item['title'])

            yield scrapy.Request(response.urljoin(detail_url), callback=self.parse_detail, meta={'item': item})

        next_page = response.css('#content > div.wp-pagenavi > a:last-child::attr(href)').extract_first()

        print('next_page %s' % next_page)

        if next_page and self.maxPage > 0:
            self.maxPage -= 1
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
        pass

    def parse_detail(self, response):
        item = response.meta['item']
        item['times'] = response.xpath('//*[@id="content"]/div[2]/div[1]/text()').re('[^\t,^\r,^\n]+')[0]
        item['first_paragraph'] = response.css('#content > div:nth-child(3) > p:nth-child(7)::text').extract_first()

        yield item
        pass
