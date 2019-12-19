import random
key = 0
punches = ['石头','剪刀','布']
def ko():
    computer_choice = random.choice(punches)
    user_choice = input('请输入你的出拳：石头、剪刀、布：')
    print('电脑的选择是：%s'% computer_choice)
    print('你的选择是：%s'% user_choice)
    if user_choice not in punches:
        print('输入有误，请重新输入')
        
    else:
        #if (computer_choice == '石头' and user_choice == '剪刀') or (computer_choice == '剪刀' and user_choice == '布') or (computer_choice == '布' and user_choice == '石头'):
        # 电脑的选择有3种，索引位置分别是：0石头、1剪刀、2布。
        # 假设在电脑索引位置上减1，对应：-1布，0石头，1剪刀，皆胜。
        '''
        index() 函数用于找出列表中某个元素第一次出现的索引位置。
        语法为：list.index(obj)，obj为object（对象）的缩写。
        '''
        if computer_choice == punches[punches.index(user_choice)-1]:
            print ('你输了')
            
        elif computer_choice == user_choice:
            print('平局')
            
        else:
            print('你赢了')
def again():
    global key
    a = input('重新开始请输入y，退出请输入其他')
    if a != 'y':
        key = 1
    print('结束')

def main():
    while key != 1:
        ko()
        again()

main()

