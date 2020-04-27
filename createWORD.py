# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:55:53 2019

@author: Administrator
根据文件列表，生成相应文件
"""

import re,docx

note = '''实验人： / 
一、实验名称：
From p - p
二、实验目的：对样本进行测序。

三、材料和设备
1.试剂和设备：
材料	物料批号	来源	用量
2×Phanta Max Master Mix	7E291C8	Vazyme	
上游测序引物	HZP20190228-1458	擎科
下游测序引物	HZP20190228-1458	擎科

2.样本

四、实验方法
1.反应体系

2.反应程序

五、实验结果

六、结论
'''

#filetype = input('请输入要输出的文件后缀名（word:docx,Excle: xlsx, 文本：txt）')
filelist = input('请输入文件列表路径：（如E:/filelist.txt）')
outputfold = input('请输入文件输出路径：')
filetype = 'docx'
# outputfold = r'd:\Desktop\NOTEbook'

# 利用replace()方法，将\替换为/
filelist.replace('\\','/')
outputfold.replace('\\','/')
n = 0
def clean_zh_text(text):
    # 去除特殊字符，留下字母、数字、汉字，并用-代替特殊字符
    comp = re.compile('[^A-Z^a-z^0-9^\u4e00-\u9fa5]')
    return comp.sub('-',text)

with open(filelist) as f:
    filenames = f.readlines()
    #print(type(filenames))
    #print(filenames)
for filename in filenames:
    filename = clean_zh_text(filename)

    # with open(outputfold + '/' + filename + '.' + filetype,'w') as f:
    #     f.write('日期：' + filename[5:] +'\n')
    #     f.write(note)
    file = docx.Document()
    file.add_paragraph('日期：' + filename[0:10] +'\n',style='List Bullet') 
    file.add_paragraph(note,style='List Bullet') #写入无序号段落
    # file.add_paragraph('结论',style='List Number') #写入有序号段落
    # file.add_picture('picture.JPG',width=docx.shared.Inches(5)) #插入图片的方法
    # table=file.add_table(rows=6,cols=6,style='Table Grid')
    # for i in range(0,6):
    #     for j in range(0,6):
    #       table.cell(i,j).text="第{i}行{j}列".format(i=i+1,j=j+1) #写入6*6表格
    file.save(outputfold + '/' + filename + '.' + filetype)
    n += 1
print('创建成功,共%s个文件'% n)        
        