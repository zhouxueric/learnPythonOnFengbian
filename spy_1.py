import requests
from bs4 import BeautifulSoup
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/'
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html,'html.parser')
# print(soup)
comments = soup.find_all(class_="comment-content")
# print(comments)
for comment in comments:
    print(comment.text)


