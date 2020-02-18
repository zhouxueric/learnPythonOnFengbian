import requests
from bs4 import BeautifulSoup

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/'
res = requests.get(url)
print(res.status_code)
html = res.text
soup = BeautifulSoup(html,'html.parser')

articles = soup.find_all('article')
for article in articles:
    time = article.find('time').text
    href = article.find('h2').find('a')['href']
    title = article.find('h2').text  #h2下只有一个text时，不需要这样写article.find('h2').find('a').text
    print(title,time,href)