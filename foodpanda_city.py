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




