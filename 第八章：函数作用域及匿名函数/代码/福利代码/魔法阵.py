import turtle as t
import pygame
import random

"""
pygame 模块是一个制作小游戏的模块，这个模块是第三方模块
我们需要去打开终端窗口
window电脑安装步骤：
1、按下win + r键打开运行窗口，然后输入cmd回车打开cmd窗口
2、在黑框框窗口中，输入pip install pygame出车去安装该模块
3、安装成功之后重启项目就可以
"""

file= '爱立刻有.mp3'
pygame.mixer.init()
pygame.mixer.music.load('python基礎學習\第八章：函数作用域及匿名函数\代码\福利代码\爱立刻有.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

def tcyuan(x,y,r):
    t.fillcolor("black")
    t.begin_fill()
    t.seth(0)
    y = y - r
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(r)
    t.end_fill()
def yuan(x,y,r):
    t.seth(0)
    y=y-r
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(r)
def yueliang():
    R = 110 -1

    r = R - 22 -1

    # 月亮填充
    t.penup()
    t.goto(-350+2*R,0)
    t.seth(90)
    t.fillcolor("black")
    t.begin_fill()
    t.circle(R,359)
    t.left(90)
    t.fd(2)
    t.left(90)
    t.circle(-r,359)
    t.left(90)
    t.fd(2)
    t.pendown()
    t.end_fill()
    #轮廓
    yuan(-350 + R, 0, R)
    yuan(-350 + 44 + r - 2, 0, r - 2)
def zhixian(R,r,count,jiaodu):
    t.seth(90+jiaodu)
#    t.goto(0, 0)
    for i in range(count):
        t.penup()
        t.goto(0, 0)
        t.fd(r)
        t.pendown()
        t.fd(R-r)
        t.left(360/count)
def zfx(R,r):
    jiange = 10
#    t.pensize(jiange)
    t.seth(90)
    big = pow((R**2)*2,0.5)
    small = big-2*jiange
    for i in range(13):
        #大线
        t.penup()
        t.goto(0,0)
        t.fd(R)
        t.pendown()
        t.right(135)
        t.fd(big)
        #小线
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd(pow((small**2)/2,0.5))
        t.pendown()
        t.right(135)
        t.fd(small)
        #粗线
        t.pensize(8)
        t.pencolor("black")
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd((R+pow((small ** 2) / 2, 0.5))/2)
        t.pendown()
        t.right(135)
        t.fd((big+small)/2)
        t.pensize(2)
        t.pencolor("yellow")
        t.seth(90+i*30)
    else:
        # 大线
        t.penup()
        t.goto(0, 0)
        t.fd(R)
        t.right(135)
        t.fd(big / 2)
        t.pendown()
        t.fd(big / 2)
        # 小线
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd(pow((small ** 2) / 2, 0.5))
        t.right(135)
        t.fd(small/2)
        t.pendown()
        t.fd(small/2)
        # 粗线
        t.pensize(8)
        t.pencolor("black")
        t.left(135)
        t.penup()
        t.goto(0, 0)
        t.fd((R + pow((small ** 2) / 2, 0.5)) / 2)
        t.right(135)
        t.fd((big + small) / 2/2)
        t.pendown()
        t.fd((big + small) / 2/2)
        t.pensize(2)
        t.pencolor("yellow")
        t.seth(90 + i * 30)
def wjx(r,jiaodu):
    t.fillcolor("black")
    t.penup()
    t.goto(0,0)
    t.seth(90+jiaodu)
    t.fd(r)
    t.pendown()
    t.right(18)
    t.begin_fill()
    for i in range(5):
        t.right(144)
        t.forward(144)
        t.left(72)
        t.forward(144)
    t.end_fill()
    if jiaodu!=0:
        t.seth(90 + jiaodu)
        for i in range(1,6):
            t.penup()
            t.goto(0, 0)
            t.left(72)
            t.pendown()
            t.fd(r)
def xingzuo():
    r = 250
    t.penup()
    t.goto(20,-35)
    t.seth(-45)
    t.fd(r)
    t.pendown()
    xz=['♒','♓','♈','♉','♌','♍','♎','♏']
    for i in range(4):
        t.write(xz[i],font=("", 20, ""))
        t.penup()
        t.right(90)
        t.circle(-300, 30)
        t.left(90)
        t.pendown()
    t.penup()
    t.goto(-r/4+10, 5)
    t.seth(135)
    t.fd(r)
    for i in range(4,8):
        t.write(xz[i],font=("", 20, ""))
        t.penup()
        t.right(90)
        t.circle(-300, 30)
        t.left(90)
        t.pendown()
def dxnb(s):
    t.penup()
    t.fd(-19)
    t.left(90)
    t.fd(2)
    t.pendown()
    t.write(s, font=["KaiTi", 30, "bold"])
def taiyang():

    def haicao(r,i):
        # 海藻
        t.fillcolor("black")

        t.penup()
        if i==0:
            t.goto(256, r)
        elif i==1:
            t.goto(256-r, 0)
        else:
            t.goto(256, -r)
        t.pendown()
        t.begin_fill()
        t.seth(2+i*90)
        t.circle(r / 2, 105)
        t.left(10)
        t.circle(-r / 3, 90)
        t.circle(r / 3, 60)
        t.left(20)
        t.circle(r / 3, -80)
        t.left(50)
        t.circle(-r + 10, -40)
        t.right(30)
        t.circle(r / 2 + 10, -50)
        t.penup()
        if i == 0:
            t.goto(256, r)
        elif i == 1:
            t.goto(256 - r, 0)
        else:
            t.goto(256, -r)
        t.pendown()
        t.end_fill()


        t.seth(2 + i * 90)
        t.circle(r / 2, 105)
        t.left(10)
        t.circle(-r / 3, 90)
        t.begin_fill()
        t.circle(r / 3, 60)
        t.left(20)
        t.circle(r / 3, -80)
        t.left(50)
        t.circle(-r + 10, -40)
        t.right(30)
        t.circle(r / 2 + 10, -50)
        t.right(30)
        t.circle(r / 2 - 2, 110)
        t.circle(-r / 3, 70)
        t.left(7)
        t.circle(r / 3, 85)
        t.end_fill()


        t.penup()
        if i == 0:
            t.goto(256, r)
            t.pendown()
            t.seth(180 - (2 + i * 90))
            t.circle(-(r / 2), 105)
        elif i == 1:
            t.goto(256 - r, 0)
            t.pendown()
            t.seth(- (2 + i * 90))
            t.circle(-(r / 2), 105)
        else:
            t.goto(256, -r)
            t.pendown()
            t.seth(180 - (2 + i * 90))
            t.circle(-(r / 2), 105)
        t.begin_fill()
        t.left(-10)
        t.circle(-(-r / 3), 90)
        t.circle(-(r / 3), 60)
        t.left(-20)
        t.circle(-(r / 3), -80)
        t.left(-50)
        t.circle(-(-r + 10), -40)
        t.right(-30)
        t.circle(-(r / 2 + 10), -50)
        t.end_fill()

        t.penup()
        if i == 0:
            t.goto(256, r)
            t.pendown()
            t.seth(180 - (2 + i * 90))
            t.circle(-(r / 2), 105)
        elif i == 1:
            t.goto(256 - r, 0)
            t.pendown()
            t.seth(- (2 + i * 90))
            t.circle(-(r / 2), 105)
        else:
            t.goto(256, -r)
            t.pendown()
            t.seth(180 - (2 + i * 90))
            t.circle(-(r / 2), 105)
        t.pendown()

        t.left(-10)
        t.circle(-(-r / 3), 90)
        t.circle(-(r / 3), 60)
        t.left(-20)
        t.begin_fill()
        t.circle(-(r / 3), -80)
        t.left(-50)
        t.circle(-(-r + 10), -40)
        t.right(-30)
        t.circle(-(r / 2 + 10), -50)
        t.right(-30)
        t.circle(-(r / 2 - 2), 110)
        t.circle(-(-r / 3), 70)
        t.left(-7)
        t.circle(-(r / 3), 85)
        t.end_fill()
    def xhaicao(r,i):
        t.penup()
        t.goto(256 + r, 0)
        t.seth(-90)
        t.circle(-r,20)
        t.pendown()
        t.begin_fill()
        t.seth(30)
        t.circle(-r/3,100)
        t.circle(r/6,140)
        t.circle(-r/11,100)
        t.left(80)
        t.circle(-r/2,-30)
        t.circle(r/4,-140)
        t.circle(-r/3,-60)
        t.end_fill()
        t.penup()
        t.goto(256 + r, 0)
        t.seth(-90)
        t.circle(-r, 30)
        t.pendown()
        t.seth(45)
        t.circle(-r / 4, 100)
        t.right(20)
        t.circle(r / 4, 140)
        t.right(10)
        t.circle(-r / 11, 90)

        t.penup()
        t.goto(256 + r, 0)
        t.seth(90)
        t.circle(r, 20)
        t.pendown()
        t.begin_fill()
        t.seth(-30)
        t.circle(-(-r / 3), 100)
        t.circle(-(r / 6), 140)
        t.circle(-(-r / 11), 100)
        t.left(-80)
        t.circle(-(-r / 2), -30)
        t.circle(-(r / 4), -140)
        t.circle(-(-r / 3), -60)
        t.end_fill()
        t.penup()
        t.goto(256 + r, 0)
        t.seth(90)
        t.circle(r, 30)
        t.pendown()
        t.seth(-45)
        t.circle(-(-r / 4), 100)
        t.right(-25)
        t.circle(-(r / 4), 140)
        t.right(-10)
        t.circle(-(-r / 11), 90)
    r = 50
    # 海藻
    haicao(r, 0)
    haicao(r, 1)
    haicao(r, 2)
    xhaicao(r,3)

    #大三角形
    t.fillcolor("black")

    for i in range(1,4):
        temp = 3
        t.penup()
        t.goto(256, 0)
        t.seth(i * 90)
        t.pendown()
        t.begin_fill()
        t.right(22.5)
        t.fd(r)
        if i==1:
            t.goto(256,3*r-temp)
            t.goto(256,0)
            t.seth(i*90+22.5)
            t.fd(r)
            t.goto(256,3*r-temp)
        elif i==2:
            t.goto(256- 3 * r+temp,0)
            t.goto(256, 0)
            t.seth(i * 90 + 22.5)
            t.fd(r)
            t.goto(256-3 * r+temp,0)
        else:
            t.goto(256, -3 * r+temp)
            t.goto(256, 0)
            t.seth(i * 90 + 22.5)
            t.fd(r)
            t.goto(256, -3 * r+temp)
        t.end_fill()
    # 小三角形
    x = pow(((2 * r) ** 2) / 2, 0.5)-8
    for i in range(1,5):
        t.penup()
        t.goto(256, 0)
        t.seth(i * 90)
        t.pendown()
        t.begin_fill()
        t.right(22.5)
        t.fd(r)
        if i==1:
            t.goto(256+x,x)
            t.goto(256,0)
            t.right(45)
            t.fd(r)
            t.goto(256+x,x)
        elif i==2:
            t.goto(256 - x, x)
            t.goto(256, 0)
            t.right(45)
            t.fd(r)
            t.goto(256 - x, x)
        elif i==3:
            t.goto(256 - x, -x)
            t.goto(256, 0)
            t.right(45)
            t.fd(r)
            t.goto(256 - x, -x)
        else:
            t.goto(256 + x, -x)
            t.goto(256, 0)
            t.right(45)
            t.fd(r)
            t.goto(256 + x, -x)
        t.end_fill()

    #圆
#    t.begin_fill()
    tcyuan(256,0,r)

def draw():
    #初始化
    t.setup(1500,800,0,0)
    t.speed(0)
    t.bgcolor("black")
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.color(r,g,b)
    t.pensize(2)
    #最大的圆
    yuan(0,0,350)
    yuan(0,0,325)
    yuan(0,0,321)
    yuan(0,0,306)
    zhixian(321,306,72,0)
    #小圆
    yuan(0,0,204)
    yuan(0,0,200)
    yuan(0,0,186)
    zhixian(200,186,72,0)
    #正方形边框以及直线
    zhixian(290,213,12,0)
    zhixian(248,205,12,15)
    zfx(306,204)
    #里五角星
    wjx(200,36)
    #月亮
    yueliang()
    #太阳
    taiyang()
    #最小圆
    tcyuan(0,328,22)
    dxnb("北")
    tcyuan(0,-328,22)
    dxnb("南")
    tcyuan(-328,0,22)
    dxnb("西")
    tcyuan(328,0,22)
    dxnb("東")

    #外五角星
    wjx(200,0)
    #星座
    xingzuo()
    t.penup()
    t.goto(-500,-500)
    t.pendown()



# 魔法阵启动代码
def run():
    t.colormode(255)
    t.ht()
    while pygame.mixer.music.get_busy():
        draw()
    t.done()

run();