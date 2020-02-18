import requests
from bs4 import BeautifulSoup

url = 'https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3'
res = requests.get(url)
print(res.status_code)
html = res.text
print(html)
soup = BeautifulSoup(html,'html.parser')
top100 = soup.find_all("div",class_="info")
# print(top100[0])
list_all = []
for info in top100:
    title = info.find("a").text
    URL = info.find("a")['href']
    # print(title,URL)
    list_all.append([title,URL])
print(list_all)
