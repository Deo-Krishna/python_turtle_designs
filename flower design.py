from turtle import *

speed(0)
def fleur():
    for i in range (188):#300
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)

fleur()
mainloop()