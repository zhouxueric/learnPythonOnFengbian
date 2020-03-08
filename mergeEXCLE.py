#_*_coding:utf-8;_*_

import os
import pandas as pd
import time

t1 = time.time()
l = []
n = 0

#查找文件位置
for file in os.walk('F:/'):   #返回元组
    print(file)
    

    #提取文件
    for table in file[2]:    #调用元组方法同列表
        path = file[0] + '/' + table    #拼接成完整路径
        data = pd.read_csv(path,header=0,encoding='utf-8',engine='python')
        n += 1
        l.append(data)
        print('第' + str(n) + '个表格已提取')


#合并表格    
date_result = pd.concat(l)
    

#导出表格 pandas.DataFrame.to_excle
date_result.to_csv('F:/date_result.csv',index=0)

t2 = time.time()
t = t2-t1
t = round(t,2)
print('用时' + str(t) + '秒')
print('完成')
