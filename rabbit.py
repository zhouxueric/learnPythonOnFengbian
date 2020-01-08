'''
问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''
'''使用真正的面向对象编程'''
class Rabbit:
    '''定义小兔子类,具有年龄属性，成长、生娃的方法'''
    def __init__(self):
        self.age = 0
    def growth(self):
        self.age += 1
    def product(self):
        '''年龄满3月，就生下小兔子，即生成新对象'''
        if self.age > 2:
            return Rabbit()
        else:
            return None
zx = Rabbit()
# 兔子祖宗
family = []
# 兔子族谱
family.append(zx)
# 祖宗入谱
mouth = 10
for i in range(mouth):
    # 每个月都族谱中小兔子都在成长、生娃
    # 每个月依次让每只小兔子成长1次，并判断是否生娃
    for member in family:
        member.growth()
        child = member.product()
        if child:
            family.append(child)
        # print(member)
number = len(family)
print(number)