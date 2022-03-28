from tkinter import *
from random import *
import math
import random

myInterface = Tk()
screen = Canvas(myInterface,width = 800, height = 500, background = "#65B4F6")
screen.pack()

y = 0
skyOptions = ["#00a1ff","#0fa5fc","#1ba8f9","#2aaff7","#3ab3f4","#46b8f2","#4fbaef","#5abeed","#62bfea","#67bfe5","#6fc3e8","#78c6e8","#81ceef","#8cd3f2","#92d3ef","#9ad4ed","#9fd4ea","#a7d5e8","#aeddef","#bae3f2","#C4E5F2","#BFE4F9"]

for i in range (len(skyOptions)):
    skyColour = skyOptions[i]
    screen.create_rectangle (0,y,905,y + 20, fill = skyColour, outline = skyColour)
    y = y + 20
   
#Bushes
for i in range(1000):
  x = randint(150,600)
  y = randint(275,425)
  size = randint(40,60)
  screen.create_oval( x, y, x + size, y + size, fill="#109910",outline="#109910")

c = [-10,400]
for b in range(1200):
  x = randint(-20,800)
  y = randint(200,425)
  s = randint(40,60)
  b = [x,y]

  distance = math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)

  if distance <= 200:
    screen.create_oval( x, y, x + s, y + s + 2, fill="chartreuse3",outline="chartreuse3")

c = [750,400]
for b in range(1000):
  x = randint(-20,800)
  y = randint(225,425)
  s=randint(30,50)
  b = [x,y]

  distance = math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)

  if distance <= 200:
    screen.create_oval( x, y, x + s, y + s + 2, fill="#5CE03E",outline="#5CE03E")

#Cloud 1
for cloud in range(1, 150):
    x = randint(50, 265)
    y = randint(0,100)
    size = randint(30,50)
    screen.create_oval( x, y, x + size, y + size, fill="white",outline="white")

#Cloud 2
for cloud in range(1, 100):
    x = randint(450, 600)
    y = randint(50,140)
    size = randint(30,50)
    screen.create_oval( x, y, x + size, y + size, fill="white",outline="white")

#Cloud 3 
for cloud in range(1, 70):
    x = randint(675, 800)
    y = randint(30,130)
    size = randint(30,50)
    screen.create_oval( x, y, x + size, y + size, fill="white",outline="white")

#Leaves
c = [650,0]
allColours = ["dark green","forest green","springgreen2","springgreen3","green2","green3","green4","chartreuse2","chartreuse3","palegreen2"]

for leaf in range(8000):
  colour = random.choice(allColours)
  x = randint(300,800)
  y = randint(0,300)
  s = randint(2,5)
  b = [x,y]
  distance = math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)

  if distance <= 200:
    screen.create_oval( x, y, x + s, y + s + 2, fill=colour,outline=colour)

c = [700,0]
for leaf in range(1000):
  colour = random.choice(allColours)
  x = randint(300,800)
  y = randint(0,300)
  s = randint(2,5)
  b = [x,y]
  distance = math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)

  if distance <= 200:
    screen.create_oval( x, y, x + s, y + s + 2, fill=colour,outline=colour)

#Tree branches
screen.create_line(650,75,575,30,fill="#3C2B25",width=8)

screen.create_line(650,75,600,100,575,120,550,125,535,120,fill="#3C2B25",width=8,smooth="true")

screen.create_line(600,100,570,130,570,135,575,150,585,170,
fill="#3C2B25",width=6,smooth="true")

screen.create_line(575,120,575,110,550,80,fill="#3C2B25",width=6,smooth="true")

screen.create_line(620,45,600,15,fill="#3C2B25",width=8)

screen.create_line(750,100,650,15,fill="#150B04",width=18)

#Leaves
c = [750,25]
for leaf in range(1500):
  colour = random.choice(allColours)
  x = randint(300,800)
  y = randint(0,300)
  s = randint(2,5)
  b = [x,y]
  distance = math.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)

  if distance <= 200:
    screen.create_oval( x, y, x + s, y + s + 2, fill=colour,outline=colour)

#Tree trunks
screen.create_polygon(710,-80,725,200,680,420,850,420,770,200,785,-80,fill="#150B04",outline="#150B04",smooth="true")

screen.create_polygon(625,-50,645,215,675,420,750,420,685,200,690,-50,fill = "#3C2B25",outline="#3C2B25",smooth="true")

#Pond
pond = screen.create_rectangle (0,400,800,500, fill = "#9BD8FB", outline = "#9BD8FB")

#Tail 
screen.create_oval(315,355,385,465,fill="#826857",outline="#826857")

#Branch that he's sitting on 
screen.create_line(120,310,170,350,250,380,300,400,400,400,500,350,575,290,650,320,700,400,width=35,smooth="true",fill="#3C2B25")

#Covering up parts of the scenery
screen.create_rectangle(500,400,800,500,fill = "#9BD8FB", outline = "#9BD8FB")
screen.create_polygon(110,325,175,340,130,275,fill="chartreuse3",outline="chartreuse3")

#Head
screen.create_oval(275,110,425,300,fill="#826857",outline="#826857")

#Arms
screen.create_oval(230,175,470,370, fill="#826857",outline="#826857")

#Body 
screen.create_oval(250,150,450,375,fill="#826857",outline="#826857")

screen.create_line(260,272,275,212,width=1)

screen.create_line(440,275,425,215,width=1)
s
screen.create_oval(255,200,445,400,fill="#FBFDC0",outline="#FBFDC0")

#Feet
screen.create_oval(280,335,325,410,fill="#826857",outline="#826857")

screen.create_oval(365,335,410,410,fill="#826857",outline="#826857")

#Eye 1
screen.create_oval(300,150,322,172,fill="white")

screen.create_oval(308,156,317,165,fill="black")

screen.create_oval(310,158,312,160,fill="white",outline = "white")

#Eye 2
screen.create_oval(370,150,392,172,fill="white")

screen.create_oval(375,156,384,165,fill="black")

screen.create_oval(377,158,379,160,fill="white",outline = "white")

#Ears
screen.create_oval(295,70,325,140,fill="#826857",outline="#826857")
screen.create_oval(370,70,400,140,fill="#826857",outline="#826857")

#Facial features
screen.create_oval(340,162,354,169,fill="black")

screen.create_line(295,174,256,165,fill="black",width = 2.5)
screen.create_line(290,179,250,174,fill="black",width = 2.5)
screen.create_line(287,184,255,183,fill="black",width = 2.5)

screen.create_line(400,174,439,165,fill="black",width = 2.5)
screen.create_line(405,179,445,174,fill="black",width = 2.5)
screen.create_line(402,184,434,183,fill="black",width = 2.5)

screen.create_line(344,180,351,180,width=1)

#Spots on body

gap = 45
x = 260
y = 240
for spot in range(3):
  x = x + gap
  screen.create_polygon(x-20,y,x,y-20,x+10,y-15,x+20,y,x+17, y,x,y-10,fill="#826857",outline="#826857",smooth="true")

x = 235
y = 265
for spot in range(4):
  x = x + gap
  screen.create_polygon(x-20,y,x,y-20,x+10,y-15,x+20,y,x+17, y,x,y-10,fill="#826857",outline="#826857",smooth="true")

screen.mainloop()