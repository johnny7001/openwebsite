# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 18:45:03 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup
import json
import time

import pymysql


#更改資料庫連線(本地端 , heroku遠端)
conn = pymysql.connect(host='localhost', user='root', password='123456789', db='web')

# conn = pymysql.connect(host='us-cdbr-east-04.cleardb.com', user='bf96b8601452c1', password='637826e7', db='heroku_674fcff7cc4475a')
cursor = conn.cursor()
# url = 'https://www.klook.com/v2/usrcsrv/popular/cards/all'
totalPage = 368
for page in range(1, totalPage+1):

    url = 'https://www.klook.com/v1/cardinfocenterservicesrv/search/platform/complete_search?sort=most_relevant&query=%E5%9C%8B%E6%97%85%E5%88%B8&page_num={}&page_size=15&is_only_total=false'.format(page)

    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
              'accept-language': 'zh_TW', 'currency': 'TWD'}

    resp = requests.get(url, headers=header)

    resp.encoding = 'utf-8'

    resp = resp.text

    data = json.loads(resp)

    result = data['result']['search_result']['cards']
    for alldata in result:
        if alldata is None:
            break
        elif 'star' in alldata['data']['review_obj'] and alldata['data']['review_obj']['star'] != None: #假設有評分且不等於None值
            title = alldata['data']['title'].replace('|', ' ').replace("'", "")#標題
            star = float(alldata['data']['review_obj']['star'])
            market_price = float(alldata['data']['price']['market_price'].replace('NT$ ', '').replace(',', '')) if alldata['data']['price']['market_price'] != None else 0.0 # 市價
            selling_price = float(alldata['data']['price']['selling_price'].replace('NT$ ', '').replace(',', ''))  # 售價
            img_url = alldata['data']['cover_url'] #圖片鏈結
            data_url = alldata['data']['deep_link'] #活動鏈結
            print('標題:{}, 評分:{}, 市價:{}, 售價:{}, 圖片:{}, 網址:{}'.format(title, star, market_price, selling_price, img_url, data_url))

            sql = "select * from klook where title = '{}'".format(title)
            cursor.execute(sql)
            conn.commit()
            if cursor.rowcount == 0:
                sql = "insert into klook (title, star, market_price, selling_price, img_url, data_url) values ('{}'," \
                      " '{}', '{}', '{}', '{}', '{}')".format(title, star, market_price, selling_price, img_url, data_url)
                cursor.execute(sql)
                conn.commit()
        else:
            title = alldata['data']['title'].replace('|', ' ').replace("'", "")  # 標題
            #假如沒有評分, 就不拆入資料庫 (評分允許為空值)
            market_price = float(alldata['data']['price']['market_price'].replace('NT$ ', '').replace(',', '')) if alldata['data']['price']['market_price'] != None else 0.0  # 市價
            selling_price = float(alldata['data']['price']['selling_price'].replace('NT$ ', '').replace(',', ''))  # 售價
            img_url = alldata['data']['cover_url']  # 圖片鏈結
            data_url = alldata['data']['deep_link']  # 活動鏈結
            print('標題:{}, 市價:{}, 售價:{}, 圖片:{}, 網址:{}'.format(title, market_price, selling_price, img_url,
                                                                    data_url))

            sql = "select * from klook where title = '{}'".format(title)
            cursor.execute(sql)
            conn.commit()
            if cursor.rowcount == 0:
                sql = "insert into klook (title, market_price, selling_price, img_url, data_url) values ('{}'," \
                      " '{}', '{}', '{}', '{}')".format(title, market_price, selling_price, img_url,
                                                              data_url)
                cursor.execute(sql)
                conn.commit()

    time.sleep(3)
conn.close()









# ticket = data['result']['data']
#
# item = ticket[0]['items']
#
# for tr in item:
#     title = tr['card_data']['title']['text']
#     image = tr['card_data']['image']['url']
#     star = tr['card_data']['review']['star']
#     selling_price = tr['card_data']['price_desc']['selling_price']
#     market_price = tr['card_data']['price_desc']['market_price']
#     text = tr['card_data']['review']['text']
#     print(title, image, star, selling_price, market_price, text)
#


