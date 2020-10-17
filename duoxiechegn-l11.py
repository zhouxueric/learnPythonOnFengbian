#第十一关
# 提示：
#1.分析数据存在哪里（打开“检查”工具，刷新页面，查看第0个请求，看【response】）
#2.观察网址规律（多翻几页，看看网址会有什么变化）
#3.获取、解析和提取数据（需涉及知识点：queue、gevent、request、BeautifulSoup、find和find_all）
#4.存储数据（csv本身的编码格式是utf-8，可以往open（）里传入参数encoding='utf-8'。这样能避免由编码问题引起的报错。)
#注：在练习的【文件】中，你能找到自己创建的csv文件。将其下载到本地电脑后，请用记事本打开，因为用Excel打开可能会因编码问题出现乱码。
from gevent import monkey
monkey.patch_all()  #将程序转化为多协程
import gevent
import requests, csv
from gevent.queue import Queue
from bs4 import BeautifulSoup

work = Queue()
# 创建队列实例
url = "http://www.mtime.com/top/tv/top100/"
work.put_nowait(url)  #将网址放入队列
url2 = "http://www.mtime.com/top/tv/top100/index-{p}.html"
for i in range(2,11):
    realUrl = url2.format(p=i)
    work.put_nowait(realUrl)
# print(work.qsize)
def clawler():
    while not work.empty():  #判断队列是否为空
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        url = work.get_nowait()  #提取队列数据
        # cookies_text = 'waf_cookie=ea964bcf-2098-4bb73e305619d21882a55f042c3c57e7507a; _ydclearance=d8fa20fd85a8514a2d5710db-a98f-416a-bf23-462ff14b8c7f-1588773825; _userCode_=20205620345283; _userIdentity_=20205620345714; _tt_=8BECDC0F66FA90CE576BDE312D634155; DefaultCity-CookieKey=974; DefaultDistrict-CookieKey=0; Hm_lvt_6dd1e3b818c756974fb222f0eae5512e=1588766626; __utma=196937584.1175628244.1588766626.1588766626.1588766626.1; __utmc=196937584; __utmz=196937584.1588766626.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=196937584.18.10.1588766626; Hm_lpvt_6dd1e3b818c756974fb222f0eae5512e=1588766887'
        # def str2dict(s):
        #     list1 = s.split(';')
        #     #print(list1)
        #     dict1 = {}
        #     for item in list1:
        #         dict1[item.split('=')[0]] = item.split('=')[1]
        #     #print(dict1)
        #     return dict1
        #     #return dict([item.split('=') for item in s.split(';')])
        # cookies = str2dict(cookies_text)
        res = requests.get(url,headers=headers)#,cookies=cookies)
        res.encoding = 'utf-8'
        print(res.status_code)
        #print(res.text)
        bs = BeautifulSoup(res.text,'html.parser')
        #print(bs)
        lists = bs.find_all('div', class_="mov_con")
        #print(li)
        for tvs in lists:
            name = tvs.text
            writer.writerow([name])
            # print(name)

csvfile = open('top100TV.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csvfile)

task_list = []

for i in range(3):
    #生成5个爬虫
    task = gevent.spawn(clawler)  #创建任务，若clawler有参数，将之作为spawn第二个参数
    task_list.append(task)
gevent.joinall(task_list) #执行所有任务



    