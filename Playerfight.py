import time,random

class Playerfight:

    def __init__(self):
        self.times = eval(input('你想进行几轮战斗？'))
    # def __init__(self,times):
    #     self.times = times 

    def rungame(self):
        self.player_life_numble = 0
        self.enemy_life_numlbe = 0
        for i in range(self.times):
            # 生成双方角色，并生成随机属性。
            print('\n-----------现在进行第%d回合战斗-----------' % (i+1))
            time.sleep(1)
            print('\n---------------【ROUND %d】-------------' % (i+1))
            time.sleep(1)
            self.player_life = random.randint(100,150)
            self.player_attack = random.randint(30,50)
            self.enemy_life = random.randint(100,150)
            self.enemy_attack = random.randint(30,50)

            # 展示双方角色的属性
            print('【玩家】\n血量：{}\n攻击：{}'.format(self.player_life, self.player_attack))
            print('------------------------')
            time.sleep(1)
            print('【敌人】\n血量：{}\n攻击：{}'.format(self.enemy_life, self.enemy_attack))
            print('------------------------')
            time.sleep(1)

            # 双方PK
            while self.player_life > 0 and self.enemy_life > 0:
                self.player_life = self.player_life - self.enemy_attack
                self.enemy_life = self.enemy_life - self.player_attack
                print('你发起了攻击，【敌人】剩余血量%s' % self.enemy_life)
                print('敌人向你发起了攻击，【玩家】剩余血量%s' % self.player_life)
                print('-----------------------')
                time.sleep(1)

            # 打印战果
            if self.player_life > 0 and self.enemy_life <= 0:
                print('敌人死翘翘了，你赢了')
                self.player_life_numble += 1
            elif self.player_life <= 0 and self.enemy_life > 0:
                print('悲催，敌人把你干掉了！')
                self.enemy_life_numlbe += 1
            else:
                print('哎呀，你和敌人同归于尽了！')
            time.sleep(1)

        # 总战果
        print('总比分   你 : 敌人 = %d : %d' % (self.player_life_numble,self.enemy_life_numlbe))
        if self.player_life_numble > self.enemy_life_numlbe:
            print('\n最终结果：你赢得了最终胜利！')
        elif self.player_life_numble < self.enemy_life_numlbe:
            print('\n最终结果：你输掉了！')
        else:
            print('\n最终结果：你和敌人平局！')

    def main(self):
        while True:
            self.rungame()
            replay = input('输入y重新开始游戏，输入其他退出')
            if replay != 'y':
                break

# zhou = Playerfight()
# # print(type(zhou))
# # zhou.main()
# # print(zhou.player_life)
# zhou.rungame()