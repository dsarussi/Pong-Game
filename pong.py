#Simple pong game in python 3

import turtle #graphic module
from Tools.demo.sortvisu import WIDTH

#window preferences
wn = turtle.Screen()
wn.title("pong by @dsarussi")
wn.bgcolor("green")
wn.setup(width=800 , height=600)
wn.tracer(0)

#score
score_a = 0
score_b=0

#paddle A / left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

#paddle B/ right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

#pen - scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier",20,"bold"))

# plus one for b
#pen_score_b = turtle.Turtle()
#pen_score_b.speed(0)
#pen_score_b.color("gold")
#pen_score_b.penup()
#pen_score_b.hideturtle()
#pen_score_b.goto(300, 180)

# functions
def paddle_a_up():
    y=paddle_a.ycor() #returns the y coordinates
    y+=20
    paddle_a.sety(y)
    
def paddle_a_down():
    y=paddle_a.ycor() #returns the y coordinates
    y-=20
    paddle_a.sety(y)
    
def paddle_b_up():
    y=paddle_b.ycor() #returns the y coordinates
    y+=20
    paddle_b.sety(y)
    
def paddle_b_down():
    y=paddle_b.ycor() #returns the y coordinates
    y-=20
    paddle_b.sety(y)
# keyboard binding
wn.listen() #listen to keyboard input
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


#main game loop
while True:
    wn.update()
    
    
    #move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    
    #border checking
    if ball.ycor() > 290: #reverse the direction of the ball when hit the top
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290: #reverse the direction of the ball when hit the right
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390: #reverse the direction of the ball when hit the left
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        #pen_score_b.write("+1", align="right", font=("courier" , 35,"bold"))
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier",20,"bold"))

    if ball.xcor() < -390: #reverse the direction of the ball when hit the left
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier",20,"bold"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx*= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx*= -1       
    
    
    
    
    