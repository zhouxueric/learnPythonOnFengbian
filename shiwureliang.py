from gevent import monkey
monkey.patch_all()
import gevent, csv, bs4, requests, time
from gevent.queue import Queue

# 生成队列
work = Queue()
url1 = 'http://www.boohee.com/food/group/'
for i in range(1,11):
    for j in range(1,11):
        real_url = url1 + str(i) + '?page=' + str(j)
        work.put_nowait(real_url)
for k in range(1,11):
    url11 = url1 + "view_menu" + '?page=' + str(k)
    work.put_nowait(url11)

#解析网页
def clawler():
    # print(work.qsize)
    while not work.empty():
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        url = work.get_nowait()
        res = requests.get(url,headers=headers)
        bs = bs4.BeautifulSoup(res.text,'html.parser')
        # print(bs)
        lists = bs.find_all('li',class_="item clearfix")
        for l in lists:
            food = l.find('h4').text
            calorie = l.find('p').text
            # print(food,calorie)
            writer.writerow([food,calorie])
#写入文件
csv_file = open('foodcalorie.csv','w',encoding='utf-8',newline='')
writer = csv.writer(csv_file)
#多协程
# time3 = time.time()
task_list = []
for i in range(10):
    task = gevent.spawn(clawler)
    task_list.append(task)
# time1 = time.time()
gevent.joinall(task_list)
# time2 = time.time()
# print(time2-time1, time1-time3)
