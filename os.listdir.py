import os, openpyxl, csv
#file_path = input('please input the path of file: ')
file_path ='d:\\Desktop\\境内第三类体外诊断试剂注册申报资料电子目'
def getlist(dir, filelist):
    newDir = dir
    if os.path.isfile(dir):
        filelist.append([dir])
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir,s)
            filelist.append([newDir])
            getlist(newDir, filelist)
    return filelist
if __name__ == '__main__':
    list = getlist(file_path, [])
    #print(list)
    #with open('rld_filelist.txt', 'a', encoding='utf-8') as f:
    #    f.writelines(list)
    
    # wb = openpyxl.Workbook()
    # sheet = wb.active
    # for l in list:
    #     print(l)
    #     li = []
    #     li.append(l)
    #     print(li)
    #     sheet.append(li)
    # wb.save('文件目录.xlsx')
    
    with open('list.csv','w',newline='') as f:
        wt = csv.writer(f,dialect='excel')
        wt.writerows(list)
    print(len(list))