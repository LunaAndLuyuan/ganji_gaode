#coding:utf-8

import bs4
from bs4 import BeautifulSoup
import requests
import urllib
from urllib.parse import urljoin
import csv
import html5lib

URL = 'http://sh.ganji.com/fang1/o%7Bpage%7Dp%7Bprice%7D/'
ADDR = 'http://sh.ganji.com/'

if __name__ == '__main__':
    start_page = 1  #开始爬取的页面
    end_page = 10   #结束爬取的页面
    price = 7       #爬取的价格
    with open('ganji.csv','w',newline='') as f: #创建一个csv文件，这种方式打开文件后，不需要手动关闭文件
        csv_writer = csv.writer(f,delimiter = ',')
        print('start...........')
        while start_page <= end_page:

            print('get:{0}'.format(URL.format(page = start_page,price = price)))
            response = requests.get(URL.format(page = start_page,price = price))
            html = BeautifulSoup(response.text,'html.parser') #第一个参数是要抓取的html文本，第二个参数指定使用的解析器
            house_list = html.select('.f-list > .f-list-item > .f-list-item-wrap') #获取房源信息

            if not house_list:
                break

            for house in house_list:
                house_title = house.select('.title > a')[0].string.encode('utf-8')
                house_addr = house.select('.address > .area > a')[-1].string.encode('utf-8')
                house_price = house.select('.info > .price > .num')[0].string.encode('utf-8')
                house_url = urljoin(ADDR,house.select('.title > a')[0]['href'])

                csv_writer.writerow([house_title,house_addr,house_price,house_url])
            start_page += 1

        print('end.............')



