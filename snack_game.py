import turtle
from time import sleep
from functools import partial
from random import randint


def pause():
    global game_is_paused
    if game_is_paused == True:
        game_is_paused = False
    else:
        game_is_paused = True

def segment(l):
    global seg
    seg = turtle.Turtle(shape="square")
    seg.hideturtle()
    seg.up()
    seg.speed(-1)
    seg.color("grey")
    l.append(seg)
    
def foodee():
    global food
    food = turtle.Turtle(shape="circle")
    food.hideturtle()
    food.speed(-1)
    food.color("red")
    food.up()
    x=randint(-360,360)
    y=randint(-260,260)
    food.goto(x,y)
    food.showturtle()

def move_up():
    if head.direction!="down":
        head.direction = "up"

def move_dn():
    if head.direction!="up":
        head.direction = "down"

def move_lt():
    if head.direction!="right":
        head.direction = "left"

def move_rt():
    if head.direction!="left":
        head.direction = "right"

def move():
    
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
    elif head.direction == "left":
        x=head.xcor()
        head.setx(x-20)
    elif head.direction == "up":
        y=head.ycor()
        head.sety(y+20)
    elif head.direction == "down":
        y=head.ycor()
        head.sety(y-20)
    


if __name__ == "__main__":
    l = []
    head = turtle.Turtle()
    #head.speed(0)
    head.direction = "right"
    head.up()
    
    wn = turtle.Screen()
    wn.bgcolor("pink")
    pen = turtle.Turtle()
    pen.up()
    pen.hideturtle()
    pen.goto(0,200)
        
    wn.setup(800, 600)
    head.shape("square")
    game_is_paused = False
    wn.listen()
    wn.onkeypress(pause, 'p')
    wn.onkeypress(move_up, "w")
    wn.onkeypress(move_lt, "a")
    wn.onkeypress(move_dn, "s")
    wn.onkeypress(move_rt, "d")
    foodee()

    while True:
        wn.update()
        
        if not game_is_paused:
            move()

            if head.xcor()>=380 or head.xcor()<=-380 or head.ycor()>=280 or head.ycor()<=-280:
                pen.write("GAME OVER")
                break
            if abs(head.xcor()-food.xcor())<=20 and abs(head.ycor() - food.ycor())<=20:
                food.hideturtle()
                segment(l)
                
                foodee()
            sleep(0.25) #if its not working properly then comment this out and non comment below sleep
            for i in range(len(l)-1,0,-1):
                x=l[i-1].xcor()
                y=l[i-1].ycor()
                l[i].goto(x,y)
                seg.showturtle()
            #sleep(0.25)    #speed depends here
            if len(l)>0:
                seg.showturtle()
                x=head.xcor()
                y=head.ycor()
                l[0].goto(x,y)
            for i in range(2,len(l)):                                               #checking collision of snake to its segments
                if head.xcor() == l[i].xcor() and head.ycor() == l[i].ycor():
                    pen.write("GAME OVER")
                    sleep(1)
                    exit()
            
            
            
        
        


    turtle.done()
