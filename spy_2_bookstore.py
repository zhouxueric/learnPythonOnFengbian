#spy_2_bookstore.py
# import re
import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
res = requests.get(url)
print(res.status_code)
html = res.text
soup = BeautifulSoup(html,'html.parser')

nav_lists = soup.find(class_="nav nav-list") #只有一个class
book_lists = nav_lists.find_all('a')
for book in book_lists:
    name = ' '.join(book.text.split())
    # print(name)

product_pods = soup.find_all(class_="product_pod") #一本书一个pod
for book in product_pods:
    name = book.find("h3").find("a") #标签h3下的a对应书名，属性title
    star = book.find("p")  #product_pod下的第一个标签p为评分，属性class两个,使用class_="star-rating"也行
    price = book.find(class_="price_color")
    print('name：%s, star-rating：%s, price：%s'% (name['title'],star['class'][1],price.text))    
