import random, time

menu = ['小青菜','白萝卜','花菜','土豆','番茄炒蛋','佛跳墙','人参炖鸡','烤猪蹄','排骨','喝粥','肯鸡鸡','阔乐','雪币','币剩克']
your_menu =[]
print('欢迎使用【随便牌】点菜系统')
time.sleep(1)
print('\n请确定你要吃的菜\n')
time.sleep(1)
while True:
    food = random.choice(menu)
    if food in your_menu:
        continue
    choice = input('吃%s吗？（输入“不”重新点菜，输入其他确定点菜）'% food)
    if choice == "不":
        continue
    else:
        your_menu.append(food)
    if len(your_menu) == len(menu):
        print('菜都被你点完啦！')
        break
    again = input('是否继续点菜？（输入“是”继续点菜，输入其他结束点菜）')
    if again != "是":
        break
print('---------------\n你点的菜单如下：')
for i in your_menu:
    print(i + ' '*(13-len(i)*2) + 'x1')
print(' '*(11-len(str(len(your_menu)))) + '共%d份'% len(your_menu))
print('---------------')
print('感谢使用【随便牌】点菜系统！')