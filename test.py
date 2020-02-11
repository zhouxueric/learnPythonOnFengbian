# from jinziqi import TicTacToe
# a = TicTacToe()
# a.main()
# import pygame
info_Dict = {1:{'书名':1,'作者':2,'推荐语':3,'状态':4,'类型':5},2:{'书名':11,'作者':12,'推荐语':13,'状态':14,'类型':15}}
for k,v in info_Dict.items():
    print(k,v)
    info_unzip = {'ID':k,'书名':v['书名'],'作者':v['书名'],'推荐语':v['推荐语'],'状态':v['状态'],'类型':v['类型']}
# print(info_unzip)        
print(info_Dict.get(1))
print(info_Dict[1]['状态'])
info_Dict[1]['状态'] = 1
print(info_Dict[1]['状态'])
print(info_Dict.get(1))