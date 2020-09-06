from scrapy import cmdline
from datetime import datetime
from colorama import init
init()
from colorama import Fore, Back, Style
import os, time, sys


class Main():
    def run(self):
        os.system('cls')
        while True:
            print(Fore.YELLOW + '当前时间: {}'.format(datetime.now()) + Style.RESET_ALL)
            title = "{}    {}    {}     {}".format(Back.WHITE + Fore.LIGHTBLUE_EX + '指数名称', Back.WHITE + Fore.LIGHTBLUE_EX + '指数数值',
                                                   Back.WHITE + Fore.LIGHTBLUE_EX + '涨跌幅',  Back.WHITE + Fore.LIGHTBLUE_EX + '涨跌数值' + Style.RESET_ALL)
            print(title)
            print("-------------------------------------------------")
            os.system('scrapy crawl index --nolog')
            print("-------------------------------------------------")
            title = "{}                      {}                  {}".format(Back.WHITE + Fore.LIGHTBLUE_EX + '基金名称', Back.WHITE + Fore.LIGHTBLUE_EX + '价格变动',
                                                        Back.WHITE + Fore.LIGHTBLUE_EX + '单价' + Style.RESET_ALL)
            print(title)
            print("-----------------------------------------------------------------")
            os.system('scrapy crawl fund --nolog')

            print(Back.RED + "当前领涨板块：" + Style.RESET_ALL)
            os.system('scrapy crawl block --nolog')
            print(Back.GREEN + "当前领跌板块：" + Style.RESET_ALL)
            os.system('scrapy crawl block1 --nolog')
            print("\n")
            for i in range(30):
                sys.stdout.write(Fore.YELLOW + "距离下次更新还有{}秒\r".format(30 - i))
                sys.stdout.flush()
                time.sleep(1)
            os.system('cls')


if __name__ == '__main__':
    Main().run()
