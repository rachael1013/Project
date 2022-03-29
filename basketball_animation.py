from tkinter import *
from time import *
from random import *

myInterface = Tk()
screen = Canvas(myInterface, width=750, height=500, background="#0C224F")
screen.pack()

#Asphalt ground
screen.create_rectangle(0,350,750,500,fill="#4F535B",outline="#4F535B")

#Stars
for i in range(100):
  x = randint(0,800)
  y = randint(0,350)
  screen.create_oval(x,y,x,y,fill="yellow",outline="yellow")

#Moon
screen.create_oval(40,40,120,120,fill="#FAFF7F",outline="#FAFF7F")

#Goalpost

screen.create_line(400,20,650,20,650,175,400,175,400,20,fill="white",width=7)

screen.create_line(450,75,600,75,600,165,450,165,450,75,fill="white",width=7)

screen.create_line(525,165,525,400,width=15)
screen.create_rectangle(450,375,600,425,fill="black")

screen.create_oval(450,115,600,165,outline="red",width=5)
screen.create_line(500,165,450,150,450,135,500,115,550,115,600,135,600,150,550,165,500,165,fill="red",width = 5,smooth="true")

#Ghost shooter
screen.create_polygon(50,250,0,300,20,350,0,400,125,400,100,250,fill="white",smooth="true")

screen.create_oval(40,285,50,295,fill="black")
screen.create_oval(70,275,80,285,fill="black")
screen.create_oval(60,300,70,315,fill="black")

screen.create_line(30,335,50,330,50,340,30,350,width=2,smooth="true")
screen.create_line(85,315,105,310,105,320,85,330,width=2,smooth="true")

#Ball
for f in range(100):
  x1 = 8*f + 100      
  x2 = x1 + 70
  y1 = 0.2*f**2 - 12*f + 200   
  y2 = y1 + 70

  ball = screen.create_oval(x1,y1,x2,y2,fill="orange")

  l1 = screen.create_line(x1,y1+35,x2,y1+35,width=2)
  l2 = screen.create_line(x1+35,y1,x1+35,y2,width = 2)
  l3 = screen.create_line(x1+18,y1,x1+30,y1+35,x1+18,y2,width=2,smooth="true")
  l4 = screen.create_line(x2-18,y1,x2-30,y1+35,x2-18,y2,width=2,smooth="true")

  screen.update()
  sleep(0.03)
  screen.delete(ball,l1,l2,l3,l4)

screen.mainloop()