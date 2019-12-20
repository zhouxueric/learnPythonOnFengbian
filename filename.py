#_*_coding:utf-8;_*_

import os
#import pandas as pd
import time

t1 = time.time()
l = []
n = 0

#查找文件位置
for file in os.walk(input('输入要导出的文件夹')):   #返回元组
    #print(file)
    
    #提取文件
    for table in file[2]:    #调用元组方法同列表
        # print(table)
        l.append(table)
    #print(l)
    with open('d:/Desktop/程序汇总/name1.xlsx','a') as f:
        for i in l:
            f.write(i + '\n')
            n += 1
    t2 = time.time()
    t = t2-t1
    t = round(t, 2)
    print('导出完成,共导出' + str(n) + '个文件,用时' + str(t) + '秒')

'''未达到的功能包括：
自动提取特定字段
持续往表格中添加，而不是替换文件 w 改成 a
筛选特定格式文件进行导出 endwith
'''

  
    
        
