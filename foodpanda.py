# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:25:43 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup

import time
import pymysql


conn = pymysql.Connect(host='localhost', user='root', passwd='123456789', db='web')

cursor = conn.cursor()



head = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'dhhPerseusGuestId=1635348087.6754290359.gUwqAhDvH; ld_key=118.232.4.162; _pxvid=8d521b55-3739-11ec-a048-6b6462567364; _gcl_au=1.1.563506115.1635348094; _ga=GA1.3.1136625943.1635348095; _fbp=fb.2.1635348095139.78439461; _pin_unauth=dWlkPU9HVXdaVEppTVRVdFltUTRZUzAwTVRjMExUZzVNRFV0TXpRMU5tVmhZakkyWkdVeg; AppVersion=a8f1fa4; __imaxuid=92c8a7d0-3739-11ec-bd0a-abda2f07ca22; hl=zh; dhhPerseusSessionId=1636271879.2873808738.vSxjnGQkgm; pxcts=94771740-3fa1-11ec-818d-734cdd3d45d7; addressConfigProviderTracked=true; _gid=GA1.3.27975070.1636272377; __imaxv=975469360.1635348099.1635854047.1636272391.6; __imaxc=1636272391.6.3.utmcsr=google|utmccn=(organic)|utmcmd=cpc|utmctr=(not provided); __imaxsync=1; _tq_id.TV-81365445-1.22cb=0a869857be5b93c1.1635348095.0.1636272801..; __imaxs=2.1636272391; __cf_bm=xvwMw9YYN4YI1sSVR2s8FSUhf0hKnBFoaNqaMZ7XQ1c-1636272804-0-AZXVjZv94RK6M5EtDTN/GzXYrGNEweQnU89K1slgeolOeBip81h86H9o0PmxDjSgRhbgPff2zgjLZN8KWPl3m8c=; _px3=8ec75f9cb79523a1856579626d07b94fe404ef902fc3fe20c0754fdc66dbd1a6:WYarLr3NOEvsX8gFPUNpRdxm9qLcOYG1gRutT+hskw+DYYx3c3gfawBO9rwOsrZAPJiZPBs6hgA9p3/sl1O8RA==:1000:HLJJKlFyiYo/gUTMjWdjFwmdu/SjBWfw4y6CK4PwJIBLOgMm9Yb9yHsZWPkC++oKc/fvHt1zyDBKplWKtj1vIEoj5ytQ3bWZf66VpWfjiu3FJ6gj04/cHIy0kgvwYZhQJZ/oDzKtcjcmWhwSLTUOwNMo9A4lIUS+PJkl/DuKOfFYOokyIvZaqAlCS8065IX5jkOTAqnomp9tpHc4U3O/0A==; _pxhd=lBA0jGOSTQ87eYViWvyomyYCQyjR9yISOYG3okOXnAYzAkVrcmxnAFZlIOd0c-VeN6N6gwIrg1GHyLgrk0S1RA; dhhPerseusHitId=1636272875396.857361409152428200.kf4b0qqtvz',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        }


city_list = dict() #建立城市清單

# 要抓取的網址
url = 'https://www.foodpanda.com.tw/'
#請求網站
list_req = requests.get(url, headers=head)
list_req.encoding = 'utf-8'

list_req = list_req.text

soup = BeautifulSoup(list_req, 'html.parser')

Allcity = soup.find('ul', class_='city-list')
for city in Allcity:
    city_url = city.find('a')
    if type(city_url) != int: #去除原始碼裡面的數字
        city_url = city.find('a').get('href')
        city_name = city_url.split('/')[2].split('-')[0]
        city_url = url + city_url

        city_list.setdefault(city_name, city_url)

    else:
        pass


city_url = list(city_list.values()) #len = 19
city_name = list(city_list.keys())




def getFoodpanda_data(city_url):
    head = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'addressConfigProviderTracked=true; dhhPerseusGuestId=1625726240.4408702442.GmccdWqdtL; ld_key=140.118.208.41; hl=en; dhhPerseusSessionId=1627183075.3261760923.4NyCItW2TA; AppVersion=c56ae2e; __cf_bm=b4ce7934e8c55f7628beb51ec8156da550d6e84a-1627183075-1800-Aau8DKX/eO1lewsBQ07uG2BnnUU/yqlOWXal75M8/cBQJO+WGD1JMV1ISno1mqnYySDl0KSkdTV+IY/chjtpCHI=; _pxhd=dEvSpWwn2ATDv8WZ7QqHtWMxKv/MksYSRbAZUt8vbVK6SpHOrN0qzhDntF4oyGsrAYt6p5aKVpjhqvrzmkr6FQ==:qtU5hZQwOoKM5J0AUwVLPnM0Z8yGHQgBSEa1nL6dTrLWaf3HXMTd2ItYO-hy2k1CjZLH2xa9Ivt5jprnHBUWXAnmLXme4UVFxxCJ-EwY88E=; dhhPerseusHitId=1627183077926.349296501302744260.osgev2xwtl',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
            }

    # 要抓取的網址

    #請求網站
    list_req = requests.get(city_url,headers = head)
    #將整個網站的程式碼爬下來
    soup = BeautifulSoup(list_req.content, "html.parser")

    city = soup.find('title').text.split('f')[0].split(' ')[-2].strip()

    getall = soup.find_all('li')
    for i in getall:
        if i.find('span',{'class':'name'}) is None:
            pass
        else:
            shopUrl = i.find('a').get('href') #鏈結
            shopName = i.find('span',{'class':'name'}).text.replace("'", " ") #店名
            img = i.find('picture').find('div').get('data-src').split('|')[0]
            star = i.find('span', class_='rating').find('strong').text #評分
            content = i.find('li', class_='vendor-characteristic').text #簡介
            delivery = i.find('li', class_='delivery-fee').text #運費
            if i.find('div', class_='tag-container') is None:
                print(city, shopUrl, shopName, img, star, content, delivery)
                time.sleep(1)
                sql = "select * from foodpanda where shopname = '{}'".format(shopName)
                cursor.execute(sql)
                conn.commit()
                if cursor.rowcount == 0:
                    sql = "insert into foodpanda (shopname, city, star, content, img, shopurl, delivery) values ('{}','{}','{}','{}','{}','{}','{}')".format(shopName, city, star, content, img, shopUrl, delivery)
                    cursor.execute(sql)
                    conn.commit()
            else:
                tag = i.find('div', class_='tag-container').text  # 標籤
                print(city, shopUrl, shopName, img, star, content, tag, delivery)
                time.sleep(1)
                sql = "select * from foodpanda where shopname = '{}'".format(shopName)
                cursor.execute(sql)
                conn.commit()
                if cursor.rowcount == 0:
                    sql = "insert into foodpanda (shopname, city, star, content, img, shopurl, delivery, tag) values ('{}','{}','{}','{}','{}','{}','{}', '{}')".format(shopName, city, star, content, img, shopUrl, delivery, tag)
                    cursor.execute(sql)
                    conn.commit()
        time.sleep(1)



for c in range(0, 19):
    getFoodpanda_data(city_url[c])
    time.sleep(1)
conn.close()




'''select star from kkday_tainan where star <> 0 order by star;''' #篩選評分!=0的資料, 並且排序
'''select avg(star) from kkday_tainan where star <> 0;''' #篩選評分 != 0 的平均值



#     shopName.append(i.find('span',{'class':'name'}).text)
#     star.append(i.find('strong').text)
#     tag.append(i.find('li',{'class':'vendor-characteristic'}).text)
#
#     part1 = i.find('li',{'class':'delivery-fee'})
#     part2 = part1.find({'strong'})
#     shipping.append(part2.text)
# print(shopName, star, tag, shipping)

# pd.DataFrame({
#     '店家名稱':shopName,
#     '評分':star,
#     '標籤':tag,
#     '外送費用':shipping
#     }).to_csv('foodpanda.csv', encoding='utf-8-sig', index=False)