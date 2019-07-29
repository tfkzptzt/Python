#2.py
from turtle import *
Pen()
bgcolor("black")
color = ['green',
         'orange',
         'red',
         'purple']
c = True
while c:
    for x in range(360):
        width(x / 50)
        pencolor(color[x % 4])
        forward(x)
        left(189)
