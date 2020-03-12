import requests
from bs4 import BeautifulSoup
from urllib.request import quote
import random
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开

movie = input('请输入电影名：')
s_movie = movie.encode('gbk')
s_movie_urls = ['http://s.ygdy8.com/plus/search.php?kwtype=0&searchtype=title&keyword='+quote(s_movie),
                   'http://s.ygdy8.com/plus/s.php?typeid=1&keyword='+quote(s_movie)]
for i in range(len(s_movie_urls)):
    s_movie_url = s_movie_urls[i]
    # print(s_movie_url)
    # url = 'http://s.ygdy8.com/plus/s.php?typeid=1&keyword='
    res = requests.get(s_movie_url)
    res.raise_for_status()
    res.encoding = 'gb2312'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    urlpart = soup.find(class_="co_content8")
    if urlpart != None:
        break
urlpart = urlpart.find_all('table')
print(urlpart)
if urlpart:
    urlpart = urlpart[0].find('a')['href']
    urlmovie = 'https://www.ygdy8.com/'+urlpart
    res1 = requests.get(urlmovie)
    res.raise_for_status()
    res1.encoding = 'gbk'
    soup_movie1 = BeautifulSoup(res1.text,'html.parser')
    urldownload = soup_movie1.find('div',id="Zoom").find('span').find('table').find('a')['href']
    print(urldownload)
else:
    print('没有' + movie)









# movies = soup.find_all('tr')
# movie_list = {}
# for movie in movies[2:12]:
#     # print(movie)
#     name = movie.find_all('a')[1].text
#     URL = movie.find_all('a')[1]['href']
#     # print(name)
#     movie_list[name] = 'https://www.ygdy8.com' + URL
# print(movie_list)
# if s_movie in movie_list.keys():
#     print(s_movie)
