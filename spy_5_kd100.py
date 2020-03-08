import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.kuaidi100.com/query/'
headers = {'Referer':'https://www.kuaidi100.com/',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
           }
params = {'type':'zhongtong', 'postid':'73119782411952', 'temp':'0.7693578972165711'}
# 快递一百增加了反爬虫，temp是系统随机参数，可以自己随机生成的，但是这个练习现在出不了正确的物流信息，所以现在当练习使用哦~后面第8关会讲到cookies的内容
res = requests.get(url, headers=headers, params=params)
print(res.url)
print(res.status_code)
# print(res.text)
json_res = res.json()
info = json_res['data']#[0]['context']
print(info)