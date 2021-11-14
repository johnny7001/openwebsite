import requests
from bs4 import BeautifulSoup
import json
import time



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


print(code_list)





