#! python3
#-*- coding: utf-8 -*-
# import os
class TicTacToe():
    '''井字棋'''
    
    def __init__(self):
        self.turn = 'X' #棋手、棋子
        self.section = [] #记录棋子位置
        print('欢迎加入井字棋游戏\n数字1-9分别代表井字的9个位置，输入相应数字即可下子。\n先手执X，后手执O')
        self.broad = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
    # def __str__():
    # #打印对象即可打印出该方法中的返回值，而无须再调用方法。

    def printbroad(self):
        '''打印棋盘'''
        print(self.broad[1], self.broad[2], self.broad[3],sep='|')
        print('-+-+-')
        print(self.broad[4], self.broad[5], self.broad[6],sep='|')
        print('-+-+-')
        print(self.broad[7], self.broad[8], self.broad[9],sep='|')

    def isinbroad(self, move):
        '''判断下子是否有效, 参数move：下子的位置'''
        if self.move not in range(1,10):
            self.move = int(input('请输入数字1-9！\n请重新输入要下子的位置'))
            return 0
        elif self.move in self.section:
            self.move = int(input('抱歉，该位置已有棋子！\n请重新输入要下子的位置'))
            return 0
        else:
            return True
        #为何连续错3次会有错误的输出，如连续3次0，则0会转出到下游

    def run(self):
        '''控制棋子'''
        self.printbroad() #打印空棋盘
        while len(self.section) < 9:
            print('轮到%s下了'% self.turn, end=',')
            try:
                self.move = int(input('输入下子位置'))
            except ValueError:
                print('输入有误！请输入数字1-9！') #避免报错：输入非int类型，会报ValueError
                continue
            else:
                # print('这是try没有产生任何异常和错误的执行的语句')
                self.isinbroad(self.move) #判断有效性
                # print(self.isinbroad(self.move))
                if self.move not in self.section and self.move in range(1,10):
                    self.section.append(self.move) #记录棋子，不能重复记录，否则列表长度不对
                    self.broad[self.move] = self.turn #写入棋子
                else:
                    continue
                # print(self.section)
            self.printbroad()
            # os.system('cls') #清屏（太彻底了）
            if self.iswin():
                print('%s赢啦！'% self.turn)
                break
            # if self.isequal():
            #     print('平局--')
            #     break
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
        else:
            print('平局--')

    def iswin(self):
        '''判断是否胜利，返回bool值：True或False'''
        #一共8种胜利的可能，用循环太麻烦，直接列出
        if self.broad[1] == self.broad[2] and self.broad[1] == self.broad[3] and self.broad[1] !=' ':
            return True
        elif self.broad[4] == self.broad[5] and self.broad[4] == self.broad[6] and self.broad[4] !=' ':
            return True
        elif self.broad[7] == self.broad[8] and self.broad[7] == self.broad[9] and self.broad[7] !=' ':
            return True
        elif self.broad[1] == self.broad[4] and self.broad[1] == self.broad[7] and self.broad[1] !=' ':
            return True
        elif self.broad[2] == self.broad[5] and self.broad[2] == self.broad[8] and self.broad[2] !=' ':
            return True
        elif self.broad[3] == self.broad[6] and self.broad[3] == self.broad[9] and self.broad[3] !=' ':
            return True
        elif self.broad[1] == self.broad[5] and self.broad[1] == self.broad[9] and self.broad[1] !=' ':
            return True
        elif self.broad[3] == self.broad[5] and self.broad[3] == self.broad[7] and self.broad[3] !=' ':
            return True
        else:
            return False
            # vaule = list(broad.values())
            # # section = []
            # for colum in [0,1,2]:
            #     if vaule[colum] == vaule[colum+1] and vaule[colum] == vaule[colum+2] \
            #             and vaule[colum] != ' ':
            #         print(turn + '胜！')
            #         break 
            #     for row in [0,3,6]:
            #         if vaule[row] == vaule[row+3] and vaule[row] == vaule[row+6] \
            #            and vaule[row] != ' ':
            #             print(turn + '胜！')
            #             break
    
    def isequal(self):
        '''判断是否提前进入平局，返回bool值：True或False
        ,有点难先不写'''
        pass

    def doagain(self):
        self.again = '是'
        while self.again == '是':
            self.__init__()
            self.run()
            self.again = input('是否再下一次？（是[/否]）')
    def main(self):
        # self.run()
        self.doagain()
        print('欢迎再次来玩')
if __name__ == '__main__':
    xiaoming = TicTacToe()
    xiaoming.main()

