import sys,time,os,playsound
from pygame import mixer
mixer.init()
mixer.music.load("E:\\20-01-2022\\abc.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
a = "hello, I am ADVIK \ncan you tell me your name to proceed further.\n "

def typewriter(a):
    for char in a:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

os.system("cls")

typewriter(a)
girlfriend = input()
if (girlfriend== "advika"):
	b = "Hello, meri jaan \nAre you excited to see your surprise?"

def typewriter(b):
    for char in b:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

os.system("cls") 

typewriter(b)
c = input()
if (c== "yes"):
	d = "ok then let's begin\nchalo ab text ko thoda lamba le jana hai is liye kewal type kiye ja rah eh taki song ka testing kar sake aaur koi baat nahi hai tumko jaisa klage waisa karna mai to wahi karunga jo test ke according sahi hoga"

def typewriter(b):
    for char in b:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.1)
        else:
            time.sleep(1)

os.system("cls") #clear

typewriter(d)
mixer.music.stop()
import turtle
import time
from pygame import mixer

mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("E:\\20-01-2022\\def.mp3") #add your music file name or path
t = turtle.Turtle()

def curve():
    t.pen(pencolor="white", pensize=3, speed=5)
    for i in range(200):
        t.rt(1)
        t.fd(1)

def love_sign():
    t.pen(pencolor="white",fillcolor="hot pink", pensize=3, speed=5)
    t.shape("turtle")
    t.shapesize(1,1,1)
    t.begin_fill()
    t.lt(50)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

    t.hideturtle()


window = turtle.Screen()
window.bgcolor('black')
window.screensize(800, 700)
window.setup(width=1.0, height=1.0, startx=None, starty=None)


mixer.music.play()

t.penup()
t.goto(-80,300)
time.sleep(1)
t.pendown()
t.shapesize(1,2,1)


t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=8)

t.begin_fill()

t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60)
t.lt(90)

t.fd(140)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(140)
t.left(90)
t.fd(60)
t.rt(90)
t.fd(25)

t.end_fill()

t.penup()
t.goto(-500,-10)
t.pendown()

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.rt(90)
t.fd(25)
t.rt(90)
t.fd(165)
t.lt(90)
t.fd(115)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(140)
t.rt(90)
t.fd(190)
t.rt(90)

t.end_fill()


t.penup()
t.fd(140)

t.fd(60)
t.pen(pencolor="white",fillcolor="cyan", pensize=3, speed=8)
t.begin_fill()

t.rt(90)
t.fd(190)
t.lt(90)
t.pendown()
t.circle(60)
t.lt(90)
t.penup()
t.fd(20)
t.rt(90)
t.pendown()
t.circle(40)
t.rt(90)
t.penup()
t.fd(20)
t.lt(90)

t.end_fill()

t.fd(80)
t.pendown()

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.lt(100)
t.fd(120)
t.rt(100)
t.fd(20)
t.rt(80)
t.fd(100)
t.lt(80)
t.fd(20)
t.lt(80)
t.fd(100)
t.rt(80)
t.fd(20)
t.rt(100)
t.fd(120)
t.rt(80)
t.fd(50)
t.lt(180)

t.end_fill()


t.penup()
t.fd(80)
t.pendown()

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.lt(90)
t.fd(120)
t.rt(90)
t.fd(80)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(80)

t.end_fill()

t.penup()
t.rt(180)

t.fd(150)
t.pendown()

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=2)
t.begin_fill()

t.lt(90)
t.fd(50)
t.lt(30)
t.fd(80)
t.rt(120)
t.fd(20)
t.rt(60)
t.fd(60)
t.lt(180)
t.rt(60)
t.fd(60)
t.rt(60)
t.fd(20)
t.rt(120)
t.fd(80)
t.lt(30)
t.fd(50)
t.rt(90)
t.fd(20)
t.rt(180)

t.end_fill()

t.penup()
t.fd(100)
t.pendown()

t.pen(pencolor="white",fillcolor="cyan", pensize=3, speed=8)
t.begin_fill()

t.circle(60)
t.lt(90)
t.penup()
t.fd(20)
t.pendown()
t.rt(90)
t.circle(40)
t.rt(90)
t.penup()
t.fd(20)
t.lt(90)

t.end_fill()

t.fd(90)
t.circle(60, extent=60)
t.pendown()

t.pen(pencolor="white",fillcolor="dark violet", pensize=3, speed=8)
t.begin_fill()

t.lt(30)

t.fd(85)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(70)
t.circle(-20, extent=180)
t.fd(70)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(85)
t.circle(40, extent=180)

t.end_fill()

t.penup()
# t.goto(300,130)
t.rt(180)
t.fd(35)
t.lt(90)
t.fd(140)
t.lt(90)
t.pendown()

love_sign()
import math  

def lovecurve(t):
    x = 16 * (math.sin(t) ** 3)
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x,y 


turtle.setup(800,700)
turtle.title("ADVIKA")
turtle.bgcolor("black")
turtle.pensize(2)
turtle.pencolor("red")
turtle.speed(0.1)

factor = 20

turtle.penup() 
for i in range(0,400):
    x, y = lovecurve(i) 
    turtle.goto(x * factor , y * factor)
    turtle.pendown()

turtle.exitonclick()
