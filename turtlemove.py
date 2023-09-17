import turtle as t

t.shape("turtle")

def move_up():
    t.setheading(90)
    t.forward(50)
    t.stamp()

def move_right():
    t.setheading(0)
    t.forward(50)
    t.stamp()
    
def move_left():
    t.setheading(180)
    t.forward(50)
    t.stamp()
    
def move_down():
    t.setheading(-90)
    t.forward(50)
    t.stamp()
    
def restart():
    t.reset()

t.onkey(move_up, "Up")
t.onkey(move_right, "Right")
t.onkey(move_left, "Left")
t.onkey(move_down, "Down")
t.onkey(restart, "Escape")
t.listen()
