# -*- coding: utf-8 -*-
import scrapy
from master.items import MasterItem
from scrapy import Request
from urllib.parse import quote
import redis,re

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['book.douban.com']
    base_url = ['http://book.douban.com/']

    def start_requests(self):
        ''' 从redis中获取，并爬取标签对应的网页信息 '''
        r = redis.Redis(host=self.settings.get("REDIS_HOST"), port=self.settings.get("REDIS_PORT"), decode_responses=True)
        while r.llen('book:tag_urls'):
            tag = r.lpop('book:tag_urls')
            url = self.base_url + quote(tag)
            yield Request(url=url,callback=self.parse,dont_filter=True) # dont_filter去重
        # pass

    def parse(self, response):
        '''解析每页图书详情地址'''
        print(response.url)
        lists = response.css(('#subject_list ul li.subject-item a.nbg::attr(href)')).extract()
        if lists:
            for i in lists:
                item = MasterItem()
                item['url'] = i
                yield item

        # #获取下一页的url地址
        # next_url = response.css("span.next a::attr(href)").extract_first()
        # #判断若不是最后一页
        # if next_url:
        #     url = response.urljoin(next_url)
        #     #构造下一页招聘列表信息的爬取
        #     yield Request(url=url,callback=self.parse)
