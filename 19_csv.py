import csv
#调用csv模块
with open('assets.csv', 'w', newline='') as csvfile:
#调用open()函数打开csv文件，传入参数：文件名“assets.csv”、追加模式“a”、newline=''。
    writer = csv.writer(csvfile, dialect='excel')
    # 用csv.writer()函数创建一个writer对象。
    header=['小区名称', '地址', '建筑年份', '楼栋', '单元', '户室', '朝向', '面积']
    writer.writerow(header)

title=input('请输入小区名称：')
address = input('请输入小区地址：')
year = input('请输入小区建造年份：')
block = input('请输入楼栋号：')


unit_loop = True
while unit_loop:
    unit=input('请输入单元号：')
    start_floor = input('请输入起始楼层：')
    end_floor = input('请输入终止楼层：')

    # 开始输入模板数据
    input('接下来请输入起始层每个房间的门牌号、南北朝向及面积，按任意键继续')

    start_floor_rooms = {}
    floor_last_number = []
    # 收集起始层的房间信息

    # 定义循环控制量
    room_loop = True
    while room_loop:
        last_number = input('请输入起始楼层户室的尾号:（如01，02）')
        floor_last_number.append(last_number)
        #将尾号用append()添加列表里，如floor_last_number = ['01','02']
        room_number = int(start_floor + last_number)
        #户室号为room_number,由楼层start_floor和尾号last_number组成,如301

        direction = int(input('请输入 %d 的朝向(南北朝向输入1，东西朝向输入2)：' % room_number ))
        area = int(input('请输入 %d 的面积，单位 ㎡ ：' % room_number))
        start_floor_rooms[room_number] = [direction,area]
        # 户室号为键，朝向和面积组成的列表为值，添加到字典里，如start_floor_rooms = {301:[1,70]}

        continued= input('是否需要输入下一个尾号？按 n 停止输入，按其他任意键继续：')
        #加入打破循环的条件
        if continued == 'n':
            room_loop = False
        else:
            room_loop = True       

    unit_rooms = {}
    #新建一个放单元所有户室数据的字典
    unit_rooms[start_floor] = start_floor_rooms
    #unit_rooms={3:{301:[1,80],302:[1,80],303:[2,90],304:[2,90]}}
    for floor in range(int(start_floor) + 1, int(end_floor) + 1):
    #遍历除初始楼层外的其他楼层
        floor_rooms = {}
        #每个楼层都建立一个字典
        for i in range(len(start_floor_rooms)):
        #遍历每层有多少个房间，这里是3，即执行for i in range 3 的循环
            number = str(floor) + floor_last_number[i]
            info = start_floor_rooms[int(start_floor + floor_last_number[i])]
            # 依次取出字典start_floor_rooms键对应的值，即面积和朝向组成的列表
            floor_rooms[int(number)] = info
            #给字典floor_rooms添加键值对，floor_rooms = {401:[1,80]}
        unit_rooms[floor] = floor_rooms
    
    with open('assets.csv', 'a', newline='')as csvfile:
    #Mac用户要加多一个参数 encoding = 'GBK'
        writer = csv.writer(csvfile, dialect='excel')
        for sub_dict in unit_rooms.values():
            for room,info in sub_dict.items():
                dire = ['', '南北', '东西']
                writer.writerow([title,address,year,block,unit,room,dire[info[0]],info[1]])   

    unit_continue = input('是否需要输入下一个单元？按 n 停止单元输入，按其他任意键继续：')
    if unit_continue == 'n':
        unit_loop = False
    else:
        unit_loop = True

print('恭喜你，资产录入工作完成！')     

'''# 公共信息
title = input('请输入小区名称')
address = input('请输入小区地址：')
year = input('请输入小区建造年份：')
block = input('请输入楼栋号：')
start_flood = input('请输入起始楼层：')
end_flood = input('请输入终止楼层：')
unit_info = {}
room_info = []
# 第1楼信息
while True:
    last_room = input('请输入户室尾号：')
    forword = input('请输入朝向：')
    area = input('请输入面积：')
    room_num = start_flood + last_room
    unit_info[room_num] = [forword, area]
    # print(unit_info)
    again = input('是否继续输入？（结束请输入q）')
    if again == 'q':
        break
# print(unit_info)

for flood in range(int(start_flood), int(end_flood)+1):
    room_num = flood + last_room
''''''
start_floor = '3'
end_floor = '4'
floor_last_number = ['01','02','03']
# 户室的尾号

start_floor_rooms = {301:[1,80], 302:[1,85], 303:[2,90]}
#初始楼层的模版数据
unit_rooms={}
#创建一个字典
unit_rooms[start_floor] = start_floor_rooms
#为新楼层创建一个字典
new_floor_rooms = {}
#先遍历户号，每循环更改1户
for room in start_floor_rooms:
    #遍历尾号
    for number in floor_last_number:
        #尾号相同，则将户型信息给新户号
        if int(number) == int(room)%100:
            #向楼层添加新户号（楼+尾号）和户型信息
            new_floor_rooms[end_floor+number] = start_floor_rooms[room]
    #print(new_floor_rooms)
unit_rooms[end_floor] = new_floor_rooms
print(unit_rooms)
''''''
start_floor = '3'
end_floor = '4'
floor_last_number = ['01','02','03']
# 之前input()输入的数据为str类型

start_floor_rooms = {301:[1,80], 302:[1,80], 303:[2,90]}
#初始楼层的模版数据

unit_rooms = {}
#创建一个字典，存储所有楼层的数据
unit_rooms[int(start_floor)] = start_floor_rooms
#unit_rooms = {3: {301: [1, 80], 302: [1, 80], 303: [2, 90]}}

floor_rooms = {}
#给4楼创建一个字典
for i in range(len(start_floor_rooms)):
    #遍历每层有多少个房间，这里是3，即执行for i in range 3 的循环
    number = '4' + floor_last_number[i]
    #字符串拼接, number = ['401','402','403']
    info = start_floor_rooms[int(start_floor + floor_last_number[i])]
    # 依次取出字典start_floor_rooms键对应的值，即面积和朝向组成的列表
    # int(start_floor + floor_last_number[0])= 301 
    # info = [1,80]

    floor_rooms[int(number)] = info
    #给字典floor_rooms添加键值对，floor_rooms = {401:[1,80]}
    #循环三次，所以floor_rooms = {401:[1,80], 402:[1,80], 403:[2,90]}

unit_rooms[4] = floor_rooms
#以4为键，floor_rooms为值，给字典unit_rooms添加键值对
print(unit_rooms)
''''''
for floor in range(int(start_floor) + 1, int(end_floor) + 1):
        #遍历除初始楼层外的其他楼层
        floor_rooms = {}
        #每个楼层都建立一个字典
        for i in range(len(start_floor_rooms)):
        #遍历每层有多少个房间，这里是3，即执行for i in range 3 的循环
            number = str(floor) + floor_last_number[i]
            info = start_floor_rooms[int(start_floor + floor_last_number[i])]
            # 依次取出字典start_floor_rooms键对应的值，即面积和朝向组成的列表
            floor_rooms[int(number)] = info
            #给字典floor_rooms添加键值对，floor_rooms = {401:[1,80]}
        unit_rooms[floor] = floor_rooms
print(unit_rooms)

''''''
unit_rooms={ 3:{301:[1,80],302:[1,80],303:[2,90],304:[2,90]},
             4:{401:[1,80],402:[1,80],403:[2,90],404:[2,90]},
             5:{501:[1,80],502:[1,80],503:[2,90],504:[2,90]}
            }

for floor in unit_rooms.values():
    # 遍历大字典的值，即小字典
    for room,info in floor.items():
        dire = ['', '南北', '东西']
        print('单元：%s,户室：%d,朝向：%s,面积：%s'% 
               (str(room)[0:-2],room,dire[info[0]],info[1]))
       
# for floor in unit_rooms:
#     #print('楼层：' + floor)
#     #for i in range(len(floor)):
        
#     print(unit_rooms[floor])
#     for room in unit_rooms[floor]:
#         unit = str(room)[0:-2]
#         # _room_info = unit_rooms[floor][room]
#         # print(_room_info)
#         # print(_room_info[0])
#         # print(unit_rooms[floor][room][0])
#         print('单元：%s'% unit)
#         print('户室：%d'% room)
#         print('朝向：%s'% unit_rooms[floor][room][0])
#         # print(unit_rooms[floor][room])
#         print('面积：%s'% unit_rooms[floor][room][1])
'''