import requests
import json
from bs4 import BeautifulSoup

res = requests.post('https://music.163.com/#/search/m/?s=%E6%B6%88%E6%84%81&type=1')
print(res.text)