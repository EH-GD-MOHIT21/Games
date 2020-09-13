def updated_ludoboard():

    import turtle

    def square(tur_name, width, height=None, color=None):
        if height == None:
            height = width
        if color != None:
            tur_name.begin_fill()
            tur_name.fillcolor(color)
        for i in range(2):
            tur_name.fd(width)
            tur_name.lt(90)
            tur_name.fd(height)
            tur_name.lt(90)
        if color != None:
            tur_name.end_fill()

    def gt(tur_name, x, y):
        tur_name.up()
        tur_name.goto(x, y)
        tur_name.down()
    # for left and right side houses

    def khanche(tur_name, l, w, temp, color, mid=None, first_color=None):
        for i in range(6):
            if temp == i or (mid == True and i != 0 and i != 5) or (color == third_color and i == 5 and mid == True) or (first_color == second_color and i == 0 and mid == True):
                tur_name.begin_fill()
                tur_name.fillcolor(color)

            square(tur_name, l, w)
            tur_name.fd(l)

            if color != None:
                tur_name.end_fill()
    # for top and bottom side houses

    def updown_khanche(tur_name, l, w, temp, color, mid=None):
        for i in range(6):
            if temp == i or (mid == True and i != 0 and i != 5) or (i == 5 and mid == True and tur_name == t1) or (i == 0 and mid == True and tur_name == t):
                tur_name.begin_fill()
                tur_name.fillcolor(color)
            square(tur_name, l, w)
            tur_name.setheading(270)
            tur_name.bk(w)
            tur_name.setheading(0)
            if color != None:
                tur_name.end_fill()

    if __name__ == "__main__":

        inp = input('want custom color enter yes if u want:').lower()

        if inp == 'yes':
            first_color = input('Enter player1 your favourite color :').lower()
            second_color = input(
                'Enter player2 your favourite color :').lower()
            third_color = input('Enter player3 your favourite color :').lower()
            fourth_color = input(
                'Enter player4 your favourite color :').lower()

            color_list = ['red', 'blue', 'green', 'cyan',
                          'yellow', 'pink', 'orange', 'violet']

            if first_color in color_list and second_color in color_list and third_color in color_list and fourth_color in color_list:
                if first_color == second_color or first_color == third_color or first_color == fourth_color:
                    print('color could not be same')
                    exit()
                else:
                    print('color updated:')
            else:
                print('color not defined')
                a = (input('enter color name to add this :'))
                try:
                    temp = turtle.Turtle()
                    temp.color(a)
                except Exception:
                    print('color not defined!!!!')
                    exit()
                else:
                    color_list.append(temp)
                    print("done successfully!!!!")
        else:
            first_color = "blue"
            second_color = "yellow"
            third_color = "red"
            fourth_color = "green"

            print('ok fine working on it!!!!')

        t = turtle.Turtle()
        wn = turtle.Screen()
        wn.setup(600, 600)
        t.speed(0)
        gt(t, -290, -290)
        t.color("pink")
        square(t, 580)

        # defining homes
        t1 = turtle.Turtle()
        t2 = turtle.Turtle()
        t3 = turtle.Turtle()
        t4 = turtle.Turtle()
        t1.speed(0)
        t2.speed(0)
        t3.speed(0)
        t4.speed(0)
        gt(t1, -290, -290)
        gt(t2, 90, -290)
        gt(t3, -290, 90)
        gt(t4, 90, 90)
        square(t1, 200, color=first_color)
        square(t2, 200, color=second_color)
        square(t3, 200, color=third_color)
        square(t4, 200, color=fourth_color)

        # home
        gt(t, -90, -90)
        t.color('black')
        square(t, 180)

        # boxes blue side
        temp = 1
        gt(t3, -290, 30)
        khanche(t3, 33.3, 60, temp, color=third_color)

        temp = 1
        gt(t3, -290, -30)
        khanche(t3, 33.3, 60, temp, color=third_color,
                mid=True, first_color=third_color)

        temp = 2
        gt(t3, -290, -90)
        khanche(t3, 33.3, 60, temp, color=first_color)

        # boxes yellow side

        temp = 3
        gt(t4, 90, 30)
        khanche(t4, 33.3, 60, temp, color=fourth_color)

        temp = 1
        gt(t4, 90, -30)
        khanche(t4, 33.3, 60, temp, color=second_color,
                mid=True, first_color=second_color)

        temp = 4
        gt(t4, 90, -90)
        khanche(t4, 33.3, 60, temp, color=second_color)

        # boxes red size

        temp = 1
        gt(t1, -90, -290)
        updown_khanche(t1, 60, 33.3, temp, color=first_color)

        temp = 1
        gt(t1, -30, -290)
        updown_khanche(t1, 60, 33.3, temp, color=first_color, mid=True)

        temp = 2
        gt(t1, 30, -290)
        updown_khanche(t1, 60, 33.3, temp, color=second_color)

        # boxes green side
        gt(t, -90, 90)

        temp = 3
        gt(t, -90, 90)
        updown_khanche(t, 60, 33.3, temp, color=third_color)

        temp = 1
        gt(t, -30, 90)
        updown_khanche(t, 60, 33.3, temp, color=fourth_color, mid=True)

        temp = 4
        gt(t, 30, 90)
        updown_khanche(t, 60, 33.3, temp, color=fourth_color)

        # houses design

        gt(t, -270, 110)
        square(t, 160, color="white")

        l = [-230, -230, -150, -150, 210, 130, 210, 130]
        for i in range(4):
            t.begin_fill()
            t.fillcolor(third_color)
            gt(t, l[i], l[i+4])
            t.circle(20)
            t.end_fill()

        gt(t1, 110, 110)
        square(t1, 160, color="white")

        l = [230, 230, 150, 150, 210, 130, 210, 130]
        for i in range(4):
            t1.begin_fill()
            t1.fillcolor(fourth_color)
            gt(t1, l[i], l[i+4])
            t1.circle(20)
            t1.end_fill()

        gt(t2, -270, -270)
        square(t2, 160, color="white")

        l = [-230, -230, -150, -150, -250, -170, -250, -170]
        for i in range(4):
            t2.begin_fill()
            t2.fillcolor(first_color)
            gt(t2, l[i], l[i+4])
            t2.circle(20)
            t2.end_fill()

        gt(t3, 110, -270)
        square(t3, 160, color="white")

        l = [230, 230, 150, 150, -250, -170, -250, -170]
        for i in range(4):
            t3.begin_fill()
            t3.fillcolor(second_color)
            gt(t3, l[i], l[i+4])
            t3.circle(20)
            t3.end_fill()

        gt(t4, 0, 0)
        theta = 45
        l = [second_color, fourth_color, third_color, first_color]
        for i in range(4):
            t4.begin_fill()
            t4.fillcolor(l[i])
            t4.setheading(theta)
            t4.fd(127)
            t4.rt(135)
            t4.fd(180)
            t4.rt(135)
            t4.fd(127)
            theta += 90
            t4.end_fill()
        t.hideturtle()
        t1.hideturtle()
        t2.hideturtle()
        t3.hideturtle()
        t4.hideturtle()
        turtle.done()


updated_ludoboard()
