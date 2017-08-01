import turtle
import random
turtle.tracer(1,0)
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()
SQUARE_SIZE=20
START_LENGTH=10

pos_list=[]
stamp_list=[] 
food_pos=[]
food_stamps=[]

snake=turtle.clone()
turtle.hideturtle()
snake.shape("square")

for i in range(START_LENGTH): 
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)

    # stamping
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'
TIME_STEP=300
SPACEBAR='space'
UP=0
DOWN=1
LEFT=2
RIGHT=3

direction=UP

UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400

def up():
    global direction
    direction=UP
    print("You pressed the up key")
    
def down():
    global direction
    direction=DOWN
    print("You pressed the down key")

def left():
    global direction
    direction=LEFT
    print("You pressed the left key")

def right():
    global direction
    direction=RIGHT
    print("You pressed the right key")

def make_food():
    food = turtle.clone()
    food.shape("trash.gif")
    food.hideturtle()
    min_x=-int (SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1

    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    food_location = (food_x,food_y)
    food_pos.append(food_location)
    food_location1=food.stamp()
    stamp_list.append(food_location1) 

make_food()

def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print('You moved right!')
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE,y_pos)
        print('You moved left!')
    elif direction==DOWN:
        snake.goto(x_pos,y_pos- SQUARE_SIZE)
        print('You moved down!')
    else:
        snake.goto(x_pos ,y_pos+SQUARE_SIZE)
        print('You moved up!')

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)
    # special place
    global food_stamps, food_pos
    
    if snake.pos()in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
        make_food()
    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    if new_x_pos>=RIGHT_EDGE:
        print('You hit the right edge! Game over!')
        quit()

    if new_x_pos<=LEFT_EDGE:
        print('You hit the left edge! Game over!')
        quit() 
    if new_y_pos<=DOWN_EDGE:
        print('You hit the down edge! Game over!')
        quit()
    if new_y_pos>=UP_EDGE:
        print('You hit the up edge! Game over!')
        quit()

    turtle.ontimer(move_snake,TIME_STEP)

move_snake()
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

turtle.register_shape('trash.gif')

food=turtle.clone()
food.shape=('trash.gif')
food_pos=[(100,100),(-100,100),(-100,-100),(100,-100)]
food_stamps=[]

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food1=food.stamp()
    food_stamps.append(food1)
    food.hideturtle()
    
