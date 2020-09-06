# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import FundItem
from tutorial.items import BlockItem
from tutorial.items import Block1Item, IndexItem
from datetime import datetime
from colorama import init
init()
from colorama import Fore, Back, Style
import json


class FundSpider(scrapy.Spider):
    fund_num = []
    f = open("cgf.csv", 'r')
    lines = f.readlines()
    for line in lines:
        code, money = line.split(",")
        fund_num.append(code)
    f.close()
    name = "fund"
    allowed_domains = ["eastmoney.com"]
    start_urls = []
    for num in fund_num:
        start_urls.append("http://fundgz.1234567.com.cn/js/{}.js".format(num))

    def parse(self, response):
        item = FundItem()
        response = response.body_as_unicode()[8:-2]
        info = json.loads(response)
        item['code'] = info['fundcode']
        item['price'] = info['gsz']
        item['percent'] = info['gszzl']
        item['name'] = info['name']
        return item


class BlockSpider(scrapy.Spider):
    name = "block"
    allowed_domains = ["eastmoney.com"]
    start_urls = ["http://86.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112408858469234434023_1598845677208&pn=1&pz=10&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:90+t:2&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f133,f104,f105&_=1598845677209"]

    def parse(self, response):
        item = BlockItem()
        response = response.body_as_unicode()[42:-2]
        info = json.loads(response)
        for i in range(5):
            item['rise_{}'.format(i + 1)] = info['data']['diff'][i]['f14']
            item['rise_{}_data'.format(i + 1)] = info['data']['diff'][i]['f3']
        return item


class BlockSpider1(scrapy.Spider):
    name = "block1"
    allowed_domains = ["eastmoney.com"]
    start_urls = ["http://11.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124010288730971399951_1598851110202&pn=1&pz=10&po=0&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:90+t:2&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f133,f104,f105,f128,f136,f207,f208,f209,f222&_=1598851110203"]

    def parse(self, response):
        item = Block1Item()
        response = response.body_as_unicode()[43:-2]
        info = json.loads(response)
        for i in range(5):
            item['drop_{}'.format(i + 1)] = info['data']['diff'][i]['f14']
            item['drop_{}_data'.format(i + 1)] = info['data']['diff'][i]['f3']
        return item

class IndexSpider(scrapy.Spider):
    name = "index"
    allowed_domains = ["http://hq.sinajs.cn/"]
    start_urls = ["http://hq.sinajs.cn/list=s_sh000001", "http://hq.sinajs.cn/list=s_sz399001", "http://hq.sinajs.cn/list=s_sz399006"]

    def parse(self, response):
        item = IndexItem()
        response = response.body_as_unicode()[23:-3]
        temp = response.split(",")
        item['name'] = temp[0]
        item['index'] = temp[1]
        item['data'] = temp[2]
        item['percent'] = temp[3]

        return item
