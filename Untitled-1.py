class Robot:
    def __init__(self):
        self.rob_name = input('	主人，我还没有名字呢，请给我起个名字吧！')
        self.my_name = input('	我该怎么称呼主人呢？')
        self.wish = input('主人有什么愿望吗？')
    def greeting(self):
        print('太好了，我有名字了！%s主人，我是%s，以后可以一直陪伴主人了' % (self.my_name,self.rob_name))
    def say_wish(self):
        print(self.my_name + '的愿望是：')
        for i in range(3):
            print(self.wish)
        
        
haha = Robot()
haha.greeting()
haha.say_wish()
    
class Chinese:  # 类的创建
    eye = 'black'  # 类属性的创建

    def __init__(self,hometown):  # 类的初始化方法
        self.hometown = hometown  # 实例属性的创建
        print('程序持续更新中……')  # 初始化中的语句
    
    def born(self):  # 实例方法的创建
        print('我生在%s。'%(self.hometown))  # 方法的具体语句

zhou = Chinese('广东')  # 类的实例化
print(zhou.eye)  # 打印实例的属性（从类传递的）
zhou.born()  # 实例方法的调用