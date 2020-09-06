# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FundItem(scrapy.Item):
    # 一般基金信息
    code = scrapy.Field()
    price = scrapy.Field()
    percent = scrapy.Field()
    name = scrapy.Field()


class BlockItem(scrapy.Item):
    rise_1 = scrapy.Field()
    rise_2 = scrapy.Field()
    rise_3 = scrapy.Field()
    rise_4 = scrapy.Field()
    rise_5 = scrapy.Field()
    rise_1_data = scrapy.Field()
    rise_2_data = scrapy.Field()
    rise_3_data = scrapy.Field()
    rise_4_data = scrapy.Field()
    rise_5_data = scrapy.Field()


class Block1Item(scrapy.Item):
    drop_1 = scrapy.Field()
    drop_2 = scrapy.Field()
    drop_3 = scrapy.Field()
    drop_4 = scrapy.Field()
    drop_5 = scrapy.Field()
    drop_1_data = scrapy.Field()
    drop_2_data = scrapy.Field()
    drop_3_data = scrapy.Field()
    drop_4_data = scrapy.Field()
    drop_5_data = scrapy.Field()


class IndexItem(scrapy.Item):
    name = scrapy.Field()
    index = scrapy.Field()
    percent = scrapy.Field()
    data = scrapy.Field()
