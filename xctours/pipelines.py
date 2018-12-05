# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XctoursPipeline(object):
    def __init__(self):
        self.file = open('datatest1.csv', 'wb')
        
    def process_item(self, item, spider):
        return item
