print("函数绘制器，输入表达式时不要忽略乘号！")
import turtle as tt
n=float(eval(input("放大倍数(整十数,建议20)=")))
t=tt.Pen()
t.pencolor("red")
t.width(n//10)
t.speed(0)
a=input("请输入函数表达式:y=")
t.penup()
for m in range(-200,201):
    x=m/n
    t.goto(n*x,n*eval(a))
    t.pendown()
t2=tt.Pen()
t2.pencolor("black")
t2.width(n//20)
t2.speed(0)
t2.penup()
t2.goto(-600,0)
t2.pendown()
t2.goto(600,0)
t2.penup()
t2.goto(0,-600)
t2.pendown()
t2.goto(0,600)
t2.penup()
for x in range(int(-800/n),int(800/n)):
    t2.goto(x*n,0)
    t2.pendown()
    t2.dot(n/4,"black")
    t2.penup()
    t2.goto(0,x*n)
    t2.pendown()
    t2.dot(n/4,"black")
    t2.penup()
    t2.goto(x*n,-800)
    t2.pendown()
    t2.goto(x*n,800)
    t2.penup()
    t2.goto(-800,x*n)
    t2.pendown()
    t2.goto(800,x*n)
    t2.penup()
