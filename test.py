# import requests
# from bs4 import BeautifulSoup
# # 图片
# # res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# # # 把Reponse对象的内容以二进制数据的形式返回
# # pic = res.content
# # with open('ppt.jpg', 'wb') as f:
# #     f.write(pic)

# # 文字
# # 下载《三国演义》第一回，我们得到一个对象，它被命名为res
# url = 'http://m.zhangyue.com/readbook/11289407/2202.html'
# res = requests.get(url)
# # res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# # 把Response对象的内容以字符串的形式返回
# print(res.status_code)
# novel = res.text
# # 现在，可以打印小说了，但考虑到整章太长，只输出800字看看就好。在关于列表的知识那里，你学过[:800]的用法。
# print(novel[:8000])

# # res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
# # # res.encoding='utf-8' #正常情况不需要
# # print(res.status_code) #响应状态
# # code = res.text
# # with open('HttpCode.txt','w',encoding='utf-8') as f:
# #     f.write(code)

# # # 音频
# # res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
# # mp3 = res.content
# # with open('Rainbow.mp3','wb') as m:
# #     m.write(mp3)

# # 获取网页源代码，得到的res是response对象。
# # res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html') 
# # # 检测请求是否正确响应
# # print(res.status_code) 
# # res.encoding='utf-8'
# # # print(res.text)
# # # 正确响应，进行读写操作
# # # 新建一个名为book的html文档，你看到这里的文件没加路径，它会被保存在程序运行的当前目录下。
# # # 字符串需要以w读写。你在学习open()函数时接触过它。
# # if res.status_code == 200:
# #     # file = open('book1.html','w',encoding='utf-8')
# #     # # res.text是字符串格式，把它写入文件内。.encode('GBK','ignore').decode('GBk') 
# #     # file.write(res.text) 
# #     # # 关闭文件
# #     # file.close() 
# #     soup = BeautifulSoup(res.text,'html.parser')
# #     # 两个方法.find(标签,属性)：查找出现的第一个和.find_all(标签,属性)：查找所有。 参数为标签、属性（或二选一）
# #     # print(type(soup))
# #     print(soup.find(class_="info"))
# #     for title in soup.find_all('a',class_="title"):
# #         print(type(title))
# #         title.

import re
a = '''B
                                Books



                                Travel

  
'''
b = a.split()
print('split:按参数切片，返回列表，无参数则按空格等字符',b)
c = re.split('[ ,\n]',a) #\n\n\n无效
# c = re.split('[\n,                                ]',a)
c = re.split(r'\n|                                ',a)
# c = re.split(r'\s+(?=[A-Z]+)',a)
print(r're.split:可用正则表达式。多字符可为"[a,b,c,\n]"或r"a|b|cd|\n",后者不限长度',c)
d = a.strip()
print('strip:去掉头尾相应字符，无参数则去空格等字符',d)
e = a.replace(' ','').replace('\n','')
print('replace:将第一个参数替换为第二个参数',e)
# 