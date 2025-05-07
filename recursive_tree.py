import turtle


def branch(t, l, w, c):
    if(w <= 0 or l <= 0):
        return
    else:
        t.pensize(w)
        t.color(c)
        t.forward(l)
        t.left(30)
        branch(t,l -40, w -2,"green")
        t.right(60)
        branch(t, l -40, w -2, "green" )
        t.left(30)
        t.back(l)

def main():
     window = turtle.Screen()
     window.screensize(1000,600)
     t= turtle.Turtle()
     t.penup()
     t.goto(0,-250)
     t.pendown()
     t.speed("fastest")
     t.left(90)

     branch(t, 180, 10, "red")
     window.exitonclick()

if __name__ =="__main__":
    main()     






