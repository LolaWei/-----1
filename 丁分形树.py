import turtle

def draw_a_tree(distance):
    if distance > 10:
        #画右边的树枝
        turtle.fd(distance)
        turtle.right(25)
        draw_a_tree(distance - 10)
        #画左边的树枝
        turtle.left(50)
        draw_a_tree(distance - 10)
        #退回到原树枝
        turtle.right(25)
        if (distance - 10) <= 10:
            turtle.color("green")
        else:
            turtle.color("black")
        turtle.bk(distance)

turtle.setup(200, 200)   #建立画布
turtle.left(90)   #将海龟方向左转90°
draw_a_tree(60)
turtle.hideturtle()
turtle.done()