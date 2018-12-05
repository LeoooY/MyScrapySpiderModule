from scrapy_redis import spiders
from xctours.InsertToRedis.Insert_Redis import insert_nextpage, insert_pagelink
from scrapy.http import HtmlResponse
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import scrapy
# slave端爬虫，对page_link字段的链接进行分布式爬取
# 并将爬取的下一页链接存入next_page字段
# next_page字段内链接交给selenium爬虫解析动态页面，提取关键信息




# http://sh.58.com/tech/33364830413903x.shtml?adtype=1&finalCp=000001230000000000000000000000000000_199761769200038328212288338&PGTID=0d303655-0000-261a-d4a7-c03585c8cc33&ytdzwdetaildj=0&entinfo=33364830413903_q&adact=3&psid=199761769200038328212288338&iuType=q_5&ClickID=2'

class nextPagespider(spiders.RedisSpider):
    name = 'nextPagespider'
    redis_key = 'page_link'

    def __init__(self):
        chr=Options()
        chr.add_argument('--diable-gpu')
        super(nextPagespider,self).__init__()
        self.driver=webdriver.Chrome(chrome_options=chr)
        # self.driver.set_window_size(500, 6000)
        dispatcher.connect(self.spider_closed,signals.spider_closed)

    def parse(self, response):
        n_test=response.xpath('//div[@id="_pg"]/a[@class="down "]/text()').extract()
        nextpage_link=response.xpath('//div[@id="_pg"]/a[@class="down "]/@href').extract()
        if nextpage_link:
            # insert_pagelink('http:'+nextpage_link[0],1)
            insert_nextpage('http:' + nextpage_link[0], 1)
            print(n_test[0],nextpage_link[0])
        print('网页：',response.url)
        # print(response.xpath('//div[@class="product_main"]/h2/a/text()').extract())
        print(response.xpath('//dl[@class="start_info"]/dd/text()').extract())
    def spider_closed(self,spider):
        print('爬取完成，退出爬虫',spider.name)
        self.driver.quit()