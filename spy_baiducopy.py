import requests
from bs4 import BeautifulSoup

res = requests.get('https://wenku.baidu.com/view/0f3c083a172ded630a1cb6c8.html')
html = res.text
print(html)
soup = BeautifulSoup(html, 'html.parser')
#pages = soup.find('div', class_="ie-fix").find('p').text
#print(pages)