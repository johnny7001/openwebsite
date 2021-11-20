import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time
url = "https://store.plusmember.jp/sakurazaka46/products/list.php?__shop_key=sakurazaka46"
header = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36'}
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

html_url = driver.page_source

next_page = driver.find_element_by_xpath('/html/body/div/div[4]/div/div/div/div/div[1]/div[2]/form/div[1]/div[2]/a[4]')
if next_page != '沒有下一頁':
    next_page.click()
    new_html = driver.page_source

else:
    print('沒有下一頁')

# resp = requests.get(url, headers=header)
# resp.encoding = 'utf-8'
# resp = resp.text
#
def get_pagegoods(html_url):
    global url
    soup = BeautifulSoup(html_url, 'html.parser')
    url_head = 'https://' + url.split('/')[2]

    total_goods = soup.find_all('li')
    for item in total_goods:
        title = item.find('p', class_='tit') #商品名稱
        price = item.find('p', class_='price') #價錢
        url = item.find('a') #購買鏈結
        img = item.find('img') #商品圖案
        sold = item.find('li', class_='ico--sold-out').text if item.find('li', class_='ico--sold-out') != None else '尚有庫存' #庫存
        delivery = item.find('li', class_='ico--reco').text if item.find('li', class_='ico--reco') != None else '通常配送'#配送方式
        new = item.find('li', class_='ico--new').text if item.find('li', class_='ico--new') != None else '' #是否為新商品
        if title is None or price is None or url is None or img is None:
            pass
        else:
            print(new)
            print(title.text)
            print(int(price.text.split('（')[0].replace('¥', '').replace(',', '').replace('\n', '')))
            print(url_head + url.get('href'))
            print(img.get('style').split('(')[1].split(')')[0])
            print(sold)
            print(delivery)
            print('-'*100)

driver.close()
# get_pagegoods(html_url)