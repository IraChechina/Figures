# Case 1
# TO DO: (Dasha) square function
pass
# TO DO:(Dasha) triangle function
pass
# TO DO:(Ira) circle function
pass
# (Dasha): figure tree
pass
# (Dasha): figure house
pass
# (Ira): figure snowman
pass
# (Ira): figure present
pass

import turtle

turtle.shape('turtle')
turtle.setup(1400, 600)


def square(x, y, a, b, color, colorinside):  # переменная квадрат
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.color(color, colorinside)
    turtle.begin_fill()
    turtle.fd(a)
    turtle.rt(90)
    turtle.fd(b)
    turtle.rt(90)
    turtle.fd(a)
    turtle.rt(90)
    turtle.fd(b)
    turtle.end_fill()
    turtle.pu()


def triangle(x, y, size, color, colorinside):  # переменная треугольник
    turtle.pu()
    turtle.setpos(x, y)
    turtle.color(color, colorinside)
    turtle.begin_fill()
    turtle.pd()
    turtle.rt(30)
    turtle.fd(size)
    turtle.rt(120)
    turtle.fd(size)
    turtle.rt(120)
    turtle.fd(size)
    turtle.rt(90)
    turtle.end_fill()
    turtle.pu()


turtle.width(3)
square(-400, 0, 200, 200, "yellow", "yellow")  # Рисуем домик
triangle(-400, 0, 200, "red", "red")  # Крыша
square(-350, -150, 100, 100, "lightblue", "lightblue")  # Окно
square(-250, -100, 100, 10, "brown", "brown")  # Оконная рама
square(-297, -50, 100, 10, "brown", "brown")

square(0, -150, 40, 50, "brown", "brown")  # Рисуем ствол ёлки
triangle(-105, -150, 250, "green", "green")  # Рисуем крону
triangle(-80, -30, 200, "green", "green")
triangle(-55, 90, 150, "green", "green")
