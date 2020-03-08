# 第一行：必不可少的调用模块。
import time

input("欢迎使用“时间管理器”！请按回车继续。")

while True:
    task_name = input('请输入任务名：')
    task_time = int(input('你觉得自己至少可以专注这个任务多少分钟？输入 N 分钟'))
    input('此次任务信息：\n我要完成的任务：%s\n我至少要专注：%d分钟\n按回车开始专注：'%(task_name,task_time))
    # 下面应该要有两行代码，自动记录可以计算以及可以打印的开始时间。
    start = time.time()
    start_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start)) 
    print('现在的时间是:'+ start_time)
    # 这里可以加一个倒计时，实时显示还剩多少时间，可参考左侧提供的资料。代码量大概有5行。
    for i in range(task_time*60,0,-1):
        info = '本次任务还需专注' + str(time.strftime('%X',time.gmtime(i)))
        print('\r' + info, end='')#\r:回到行首，并覆盖输出，达到单行输出效果，此处加入闪烁,\r可不要。
        print('\b'*len(info)*3, end='', flush=True)#闪烁效果
        time.sleep(1)
    # '''另1种方式：倒计时中，以任务时间为循环条件，输出的时间应该是当前时间与
    # 任务开始时间的差值转换成的分钟，当差值大于任务时间时循环结束'''
    # while True:
    #     remain_time = task_time*60 + start - time.time()
    #     if remain_time < 0:
    #         break
    #     print('\r本次任务还剩%s'% time.strftime('%X',time.gmtime(remain_time)),end='',flush=True)
    #     time.sleep(1)
    print('本次任务时间到')

    task_status = input('请在任务完成后按输入y:')
    # actual_time = int(input('该任务实际用时为几分钟？'))
    if task_status == 'y':
        # 下面应该要有两行代码，自动记录可以计算以及可以打印的结束时间。
        end = time.time()
        print('任务结束的时间是:'+time.strftime('%X',time.localtime(end)))
        actual_time = time.strftime('%M:%S',time.gmtime(end-start))
        # 有了自动记录的始末时间后，记录的代码也需要随之改变。
        with open('timelog2.txt','a', encoding = 'utf-8') as f:
            f.write(task_name + ' 的预计时长为：' + str(task_time) + '分钟\n')
            f.write(task_name + ' 的实际时长为：' + str(actual_time) + '分钟\n')
        again = input('建立一个新任务请按 y, 退出时间日志记录器请按 q：')
        if again == 'q':            
            break
    else:
        print('抱歉，你的输入有误。请重启时间记录器。')

print('愿被你善待的时光，予你美好的回赠。')
