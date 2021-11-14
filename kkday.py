import requests
from bs4 import BeautifulSoup
import json
import time

import pymysql

conn = pymysql.connect(host='us-cdbr-east-04.cleardb.com', user='bf96b8601452c1', password='637826e7', db='heroku_674fcff7cc4475a')
cursor = conn.cursor()

url = 'https://www.kkday.com/zh-tw/area_api/ajax_get_page_data?countryCode=A01-001&cityCode='

resp = requests.get(url)

resp.encoding='utf-8'

resp = resp.text

data = json.loads(resp)

Allcity = data['data']['hot_cities']

code_list = dict()

for city in Allcity:
    code = city['code']
    name = city['urlName']
    code_list.setdefault(name, code)


#以下為可串接的參數
param = {'city': 'A01-001-00003',
'row': '15',
'glang': '',
'cat': '',
'availstartdate': '',
'availenddate': '' ,
'fprice': '*',
'eprice': '*',
'sort': 'pasc',
'page': '1'}

code = list(code_list.values()) #取出values並且轉list, len=25

city_name = list(code_list.keys())

print(city_name)
def city_data(city_name, code): #code = 城市的代碼
    page = 1
    while 1: #進行無限迴圈, 直到判斷資料為[]的時候跳出
        url = 'https://www.kkday.com/zh-tw/product/ajax_productlist/A01-001?city={}&row=15&glang=&cat=&availstartdate=&availenddate=&fprice=&eprice=&sort=&page={}'.format(code, page)

        header = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36',
                  'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                  'accept': 'application/json, text/plain, */*'}

        resp = requests.get(url, headers=header)

        resp.encoding = 'utf-8'

        resp = resp.text

        data = json.loads(resp)

        page_j = len(data['data'])
        if data['data'] != []:
        # print(data['data'][0])
            for journey in range(0, page_j):
                Alljourney = data['data'][journey]
                title = Alljourney['name'].replace("|", " ").replace("'", " ") #標題
                content = Alljourney['introduction'].replace("'", " ") #簡介
                rating_count = int(Alljourney['rating_count']) #評論數
                star = float(Alljourney['rating_star']) #顆星
                order_count = int(Alljourney['order_count']) #已訂購數
                market_price = int(Alljourney['sale_price']) #原本的價格
                selling_price = int(Alljourney['price']) #實際售價
                img_url = Alljourney['img_url']
                data_url = Alljourney['url']
                print(title)
                print(content)
                print(rating_count)
                print(star)
                print(order_count)
                print(market_price, selling_price, img_url, data_url)


                #假如table不存的的話就見建立, else 搜尋裡面使否有已經存在的值

                sql = "CREATE TABLE IF NOT EXISTS kkday_{}(id int not null auto_increment, title varchar(255), content LONGTEXT,  rating_count int, star float, order_count int, market_price int, selling_price int, img_url varchar(255), data_url varchar(255), primary key(id))".format(city_name)
                cursor.execute(sql)
                conn.commit()

                sql = "select * from kkday_{} where title = '{}'".format(city_name, title)
                cursor.execute(sql)
                conn.commit()

                if cursor.rowcount == 0:
                    sql = "insert into kkday_{} (title, content, rating_count, star, order_count, market_price, selling_price, img_url, data_url) values ('{}'," \
                          " '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(city_name, title, content, rating_count, star, order_count, market_price, selling_price, img_url, data_url)
                    cursor.execute(sql)
                    conn.commit()


            time.sleep(5)
            page += 1
        else:
            break


# city_data('pingtung', 'A01-001-00015')
# #共25縣市
#
# # for c in range(19, 25): #迴圈抓取全部縣市
# #     city_data(city_name[c].replace("-", ""), code[c])
# #     time.sleep(5)
# conn.close()
