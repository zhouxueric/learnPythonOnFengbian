import turtle, math

def mian(width,high):
    turtle.color("red","red")
    turtle.begin_fill()
    for i in range(2):
        # x = 300
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(high)
        turtle.right(90)
    turtle.end_fill()
def star(x,y,r,s):
    # x,y轴坐标，半径 * 分段的大小
    
    turtle.pencolor("yellow")
    turtle.pensize(r*s/10)
    turtle.penup()
    print('begin')
    dis = displacement(x,y,r,s)
    # print(dis)
    print(dis['x'],dis['y'],dis['l'])
    turtle.goto(dis['x'],dis['y'])
    # print(px,py)
    turtle.pendown()
    for _ in range(5):
        turtle.fd(dis['l'])
        turtle.rt(144)

def displacement(x,y,r,s):
    '''计算大星与小星的偏转距离,画笔起始点需在两星连线上
    返回字典{'x':px, 'y':py, 'i':pl}'''
    # global ratio
    l = 2*r*math.cos(18/180*math.pi)
    pl = l*s
    # print('pl',pl)
    if big_x == x: #相对大星无水平移动，大星自身
        px = x*s
        # print('px',px)
        py = -(y-r)*s  #上方为正多移动r，正方为负少移动r
        if y - big_y < 0:
            py = -1*(y+r)*s
        # print('py',py)
    elif big_y == y: #相对大星无竖直移动
        px = (x-r)*s
        py = -y*s
        if x - big_x < 0:  #左方为正多移动r，右方为负少移动r
            px = (x+r)*s
    else:
        ratio = (big_y - y) / (x - big_x) #计算tan的比值
        # print('ratio', big_y - y, x - big_x )
        px = (x - r*math.cos(math.atan(ratio))) *s
        # print('px',px)
        py = -(y + r*math.sin(math.atan(ratio))) *s
    # print(px, py, pl)
    return {'x':px, 'y':py, 'l':pl}

width = 300
high = width/3*2  #旗面宽高3:2
segment = width/30 #旗面分割成30*20个正方形小格
big_x, big_y, big_r = 5, 5, 3  #大五星 外接圆心,半径（5，5，3）
s1_x, s1_y, s1_r = 10, 2, 1
s2_x, s2_y, s2_r = 12, 4, 1
s3_x, s3_y, s3_r = 12, 7, 1
s4_x, s4_y, s4_r = 10, 9, 1

turtle.screensize(bg="green")
turtle.setup(width=660,height=440, startx=700, starty=100)
turtle.speed(6)
mian(width,high)

turtle.rt(72)
star(big_x, big_y, big_r, segment)
turtle.undo()  #撤销最后一步的rt(144)度,或者下面angle-144也行
# turtle.penup()
angle = 72 - 180*math.atan((big_y - s1_y) / (s1_x - big_x))/math.pi  #用反正切函数求角度
turtle.rt(angle) #大星与小星1a中心的偏转角度
# turtle.pendown()
star(s1_x, s1_y, s1_r, segment)
angle1 = 180/math.pi * (math.atan((big_y - s1_y) / (s1_x - big_x)) -math.atan((big_y - s2_y) / (s2_x - big_x)))
turtle.rt(angle1)
# print(angle1)
star(s2_x, s2_y, s2_r, segment)

turtle.rt( 180/math.pi * (math.atan((big_y - s2_y) / (s2_x - big_x)) -math.atan((big_y - s3_y) / (s3_x - big_x))) )
star(s3_x, s3_y, s3_r, segment)

turtle.rt( 180/math.pi * (math.atan((big_y - s3_y) / (s3_x - big_x)) -math.atan((big_y - s4_y) / (s4_x - big_x))) )
star(s4_x, s4_y, s4_r, segment)
turtle.hideturtle()
turtle.mainloop()