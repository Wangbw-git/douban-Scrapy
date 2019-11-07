# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re,redis

class MasterPipeline(object):
    def __init__(self,host,port):
        #连接redis数据库
        self.r = redis.Redis(host=host,port=port,decode_responses=True)

    @classmethod
    def from_crawler(cls,crawl): # cls代表这个类
        '''注入实例化对象（传入参数）'''
        return cls(
            host = crawl.settings.get("REDIS_HOST"),
            port = crawl.settings.get("REDIS_PORT"),
        )

    def process_item(self, item, spider):
        #使用正则判断地址是否有效，并写入redis
        bookid = re.findall("book.douban.com/subject/([0-9]+)/",item['url'])
        if bookid:
            if self.r.sadd('books:id',bookid[0]):
                self.r.lpush('bookspider:start_urls',item['url'])
        else:
            self.r.lpush('bookspider:no_urls',item['url'])
        return item
