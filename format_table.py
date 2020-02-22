# -*- coding: utf-8 -*-
"""
Spyder Editor

将按列保存的样本，转换成每行n个的矩阵排列。
"""

with open('d:\\desktop\\sample.txt') as sample:
    lines = sample.readlines()

i = 0    
separate = '\t'  #分隔符用tab还是其它符号
#num = int(input('列数:'))   #列数
num = 8
result = []
for line in lines:
    line = line.strip('\n')
    i += 1
    result.append(line + separate)
    if i % num ==0:
       result.append('\n')
print('转换成功，共%s个' % i)

with open('d:\\desktop\\format_sample.txt','w') as f:
    f.writelines(result)
    f.wri