from tkinter import *
from time import *
from random import *

myInterface = Tk()
screen = Canvas(myInterface,width = 500, height = 500,background = "black")
screen.pack()

screen.create_rectangle(0,400,500,500,fill="white")

for r in range(125):
  a = randint(0,500)
  b = randint(0, 500)
  snow = screen.create_oval(a,b,a+5,b+5,fill = "white",outline = "white")

screen.create_text(60,40,text="Merry Christmas!",font=("Times",30,"bold"),anchor = W,fill="green")

E = 300
eSpeed = -3
S = (360-E)/2
x = 0
y = 200
r = 50

x1 = x-r
y1 = y-r
x2 = x + r
y2 = y + r

for f in range(2000):
  pacman = screen.create_arc(x1,y1,x2,y2,start = S,extent = E,fill="yellow")

  hat = screen.create_polygon(x,85,x-40,y1+5,x+40,y1+5,fill="red")

  pompom = screen.create_oval(x-9,98,x+9,80,fill = "white",outline = "white")

  c1 = screen.create_oval(x-43,y1-10,x+43,y1+10,fill = "white",outline = "white")

  screen.update()
  sleep(0.03)

  screen.delete(pacman,hat,pompom,c1)
  
  if E <= 300 or E >= 360:
    eSpeed = -1 * eSpeed

  E = E + eSpeed
  S = (360-E)/2
  x1 = x1 + 4
  x2 = x2 + 4
  x = x + 4
  

screen.mainloop()
