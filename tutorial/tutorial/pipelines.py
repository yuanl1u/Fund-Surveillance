# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from __future__ import print_function, unicode_literals
from wcwidth import wcswidth as ww
import sys
sys.path.append('C:\\Users\\GerrardLiu\\PycharmProjects\\Fund\\tutorial\\tutorial')
from colorama import init
init()
from colorama import Fore, Back, Style
from tutorial.items import FundItem, BlockItem, Block1Item, IndexItem


def rpad(s, n, c=' '):
    return s + (n-ww(s)) * c  # 对齐


init(autoreset=True)
init(wrap=True)


class TutorialPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, FundItem):
            # profit = 0
            # cur_money = 0
            temp = dict(item)
            # f = open("cgf.csv", 'r')
            # lines = f.readlines()
            # for line in lines:
            #     code, money = line.split(",")
            #     if code == item['code']:
            #         cur_money = money
            # f.close()
            temp_list = [temp['name'], temp['percent'], temp['price']]
            if temp_list[1][0] == '-':
                # profit = float(temp_list[1]) * 0.01 * cur_money
                # print(profit)
                temp_list[1] = (Fore.GREEN + temp_list[1] + "%" + Style.RESET_ALL)
            else:
                temp_list[1] = (Fore.RED + "+" + temp_list[1] + "%" + Style.RESET_ALL)
            out = "{} {} {}".format(rpad(temp_list[0], 30), rpad(temp_list[1], 15), rpad(temp_list[2], 10))
            print(out)
            print("-----------------------------------------------------------------")

            return item

        elif isinstance(item, BlockItem):
            temp = dict(item)
            for i in range(5):
                name = temp["rise_{}".format(i + 1)]
                data = temp["rise_{}_data".format(i + 1)]
                if i < 4:
                    print(name, "+", data, "%", "、", end='')
                else:
                    print(name, "+", data, "%")

            return item

        elif isinstance(item, Block1Item):
            temp = dict(item)
            for i in range(5):
                name = temp["drop_{}".format(i + 1)]
                data = temp["drop_{}_data".format(i + 1)]
                if i < 4:
                    if data < 0:
                        print(name, data, "%", "、", end='')
                    else:
                        print(name, "+", data, "%", "、", end='')
                else:
                    if data < 0:
                        print(name, data, "%")
                    else:
                        print(name, "+", data, "%")
            return item

        elif isinstance(item, IndexItem):
            temp = dict(item)
            temp_list = [temp["name"], temp["index"], temp["percent"], temp["data"]]
            if temp_list[2][0] == '-':
                temp_list[0] = (Fore.GREEN + temp_list[0] + Style.RESET_ALL)
                temp_list[1] = (Fore.GREEN + temp_list[1] + "↓" + Style.RESET_ALL)
                temp_list[2] = (Fore.GREEN + temp_list[2] + "%" + Style.RESET_ALL)
                temp_list[3] = (Fore.GREEN + temp_list[3] + Style.RESET_ALL)
            else:
                temp_list[0] = (Fore.LIGHTRED_EX + temp_list[0] + Style.RESET_ALL)
                temp_list[1] = (Fore.LIGHTRED_EX + temp_list[1] + "↑" + Style.RESET_ALL)
                temp_list[2] = (Fore.LIGHTRED_EX + temp_list[2] + "%" + Style.RESET_ALL)
                temp_list[3] = (Fore.LIGHTRED_EX + temp_list[3] + Style.RESET_ALL)
            out = "{} {} {} {}".format(rpad(temp_list[0], 2), rpad(temp_list[1], 3), rpad(temp_list[2], 2), rpad(temp_list[3], 2))
            print(out)
            return item
