
# coding: utf-8

# In[ ]:


#Importing modules
import turtle
import random

#defining turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.pencolor("purple")

#Deciding how many times it will be run and the x,y center location shapes
for n in range(50):
    x = random.randrange(-turtle.window_width()//2,
                        turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    
    #Making sure we are not drawing when moving to new location
    t.penup()
    t.setpos(x,y)
    t.pendown()
    
    #When on right place starting to draw
    for m in range(x,y):
        t.forward(m*2)
        t.left(100)

