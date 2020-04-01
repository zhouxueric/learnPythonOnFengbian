import turtle
from math import pi
# https://blog.csdn.net/zengxiantao1994/article/details/76588580
# turtle.screensize(canvwidth=None, canvheight=None, bg=None)，参数分别为画布的宽(单位像素), 高, 背景颜色。
# turtle.screensize(1366,768, "green")#
# # turtle.setup(width=0.5, height=0.75, startx=None, starty=None)，参数：width, height: 输入宽和高为整数时, 表示像素; 为小数时, 表示占据电脑屏幕的比例，(startx, starty): 这一坐标表示矩形窗口左上角顶点的位置, 如果为空,则窗口位于屏幕中心。
# turtle.setup(width=0.8,height=0.8,startx=0, starty=0)
turtle.setup(width=900,height=600, startx=100, starty=100)

# # 画笔(画笔的属性，颜色、画线的宽度等)
# turtle.pensize(12) #：设置画笔的宽度；
# turtle.pencolor('red') #：没有参数传入，返回当前画笔颜色，传入参数设置画笔颜色，可以是字符串如"green", "red",也可以是RGB 3元组。
# turtle.speed(10) #：设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快。
# turtle.hideturtle()

# # # 画正方形
# # a = turtle.Turtle()
# # for i in range(5):
# #     a.fd(100)
# #     a.lt(90)
# # turtle.mainloop()

# # 画圆，n足够大时为圆，n小时为正多边形
# b = turtle.Turtle()
# r = 10
# n = 4
# for i in range(n):
#     b.fd(2*pi*r/n)
#     b.lt(360/n)
# turtle.mainloop()

# turtle.screensize(bg="red")
# c = turtle.Turtle()
# # c.fillcolor("yellow")
# # c.pencolor("red")
# c.color("yellow", "yellow") #同时设置pencolor=color1, fillcolor=color2
# c.pensize(2)
# c.penup()
# c.setx(-200)
# c.sety(150)
# c.pendown()
# c.begin_fill()
# n = 5
# for i in range(n):
#     c.forward(200)
#     c.left(-144)
# c.end_fill()
# turtle.mainloop()


from datetime import *
 
# 抬起画笔，向前运动一段距离放下
def Skip(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()
 
def mkHand(name, length):
    # 注册Turtle形状，建立表针Turtle
    turtle.reset()
    Skip(-length * 0.1)
    # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    turtle.end_poly()
    # 返回最后记录的多边形。
    handForm = turtle.get_poly()
    turtle.register_shape(name, handForm)
 
def Init():
    global secHand, minHand, hurHand, printer
    # 重置Turtle指向北
    turtle.mode("logo")
    # 建立三个表针Turtle并初始化
    mkHand("secHand", 135)
    mkHand("minHand", 125)
    mkHand("hurHand", 90)
    secHand = turtle.Turtle()
    secHand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    hurHand = turtle.Turtle()
    hurHand.shape("hurHand")
   
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
   
    # 建立输出文字Turtle
    printer = turtle.Turtle()
    # 隐藏画笔的turtle形状
    printer.hideturtle()
    printer.penup()
    
def SetupClock(radius):
    # 建立表的外框
    turtle.reset()
    turtle.pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            turtle.forward(20)
            Skip(-radius - 20)
           
            Skip(radius + 20)
            if i == 0:
                turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
            elif i == 30:
                Skip(25)
                turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
                Skip(-25)
            elif (i == 25 or i == 35):
                Skip(20)
                turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
                Skip(-20)
            else:
                turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
            Skip(-radius - 20)
        else:
            turtle.dot(5)
            Skip(-radius)
        turtle.right(6)
        
def Week(t):   
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]
 
def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)
 
def Tick():
    # 绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)
    
    turtle.tracer(False) 
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.home()
    turtle.tracer(True)
 
    # 100ms后继续调用tick
    turtle.ontimer(Tick, 100)
 
def main():
    # 打开/关闭龟动画，并为更新图纸设置延迟。
    turtle.tracer(False)
    Init()
    SetupClock(160)
    turtle.tracer(True)
    Tick()
    turtle.mainloop()
 
if __name__ == "__main__":
    main()