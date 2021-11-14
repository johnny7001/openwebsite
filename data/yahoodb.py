# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 19:38:11 2021

@author: USER
"""

import db

from bs4 import BeautifulSoup
import requests

from datetime  import datetime

today = datetime.today()
getdate = today.strftime("%Y-%m-%d")


url ='https://tw.buy.yahoo.com/search/product?p=ps5'

data = requests.get(url)
data.encoding = 'UTF-8'

data = data.text




soup = BeautifulSoup(data,'html.parser')    

product = soup.find_all('li',class_='BaseGridItem__grid___2wuJ7 BaseGridItem__multipleImage___37M7b')

for row in product:
    link = row.find('a').get('href')
    img = row.find('img').get('srcset')
    img = img.split()[0]
    title = row.find('span',class_='BaseGridItem__title___2HWui').text
    price = row.find('em').text
    price = price.replace('$','')
    price = price.replace(',','')
    
    sql = "select id,price from shop where link='{}'".format(link)
    db.cursor.execute(sql)
    db.conn.commit()
    
    if db.cursor.rowcount == 0:
        sql ="insert into shop(shop,title,link,img_url,price,create_data) values('Yahoo','{}','{}','{}','{}','{}')".format(title,link,img,price,getdate)
        db.cursor.execute(sql)
        db.conn.commit()        
    else:
        result = db.cursor.fetchone()
        if price != result[1]:
            sql = "update shop set price='{}' where id='{}'".format(price,result[0])
            db.cursor.execute(sql)
            db.conn.commit()            
            
            
            
        
    
db.conn.close()    
    
