from turtle import *
color("red")
shape("turtle")
speed(15)
pensize(6)
Screen().bgcolor("purple")
def formev():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)

def brancheFlocon():
    for x in range(0,4):
        forward(30)
        formev()
    backward(120)

def flocon():
    for x in range(0,6):
        brancheFlocon()
        right(60)
flocon()

for x in range(0,18):
    brancheFlocon()
    right(20)

hideturtle()
    
