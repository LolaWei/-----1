import turtle as t
def draw_octagon(size):
    count=0
    while count<=8:
        t.forward(size)
        t.right(45)
        count+=1
    if size<=200:
        size+=50
        draw_octagon(size)

def write_characters(s):
    t.penup()
    t.goto(100,-200)
    t.pendown()
    t.color("pink")
    t.write(s,font=("arial",20,"bold"))

def main():
    t.penup()
    t.left(270)
    t.forward(100)
    t.pendown()
    t.pensize(25)
    t.color("pink")
    draw_octagon(60)
    write_characters("看起来好像一朵玫瑰花！")
    t.done()

if __name__=="__main__":
    main()




