# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis import spiders
from xctours.InsertToRedis.Insert_Redis import insert_pagelink,insert_nextpage

# 从城市分类页爬取每个城市旅游信息的起始页链接，存入master端page_link字段，
# 交给slave端nextpage_spider爬取每个下一页的链接
# 链接存入Redis的工具包：InsertToRedis.Insert_redis

class Xcspider01(spiders.RedisSpider):
    name = 'xcspider01_redis'
    #allowed_domains = ['ctrip.com']
    redis_key = 'xcspider01:start_urls'

    #start_urls = ['http://vacations.ctrip.com/tours']

    def parse(self, response):
        for each in response.xpath('//div[@class="sel_list"]/dl/dd/a'):
            a=each.xpath('text()').extract()[0]
            page_link=each.xpath('@href').extract()[0].replace('/you','http://vacations.ctrip.com/tours',1)
            if page_link:
                insert_pagelink(page_link,1)
                insert_nextpage(page_link,1)#记录已爬链接
                print(a," 的链接为 ",page_link," 已插入")

