import turtle
    
_t = turtle.Turtle()

class Draw_shapes:
    def draw_circle(self, _t, _x, _y, tilt, radius, extent, fillcolor, pencolor):
        """
        This is the atomic shape circle used for the ball on the sword and the shield in various places throughout.
        _x, and _y are for coordinates
        radius is used for the circle size
        fillcolor is for the color inside of the circles
        pencolor is for the circle borders
        """
        _t.up()
        _t.goto(_x,_y)
        _t.setheading(tilt)
        _t.down()
        _t.color(pencolor, fillcolor)
        _t.begin_fill()
        _t.circle(radius, extent)
        _t.end_fill()
        _t.speed(0)

    def draw_rectangle(self, _t, _x, _y, height, width, tilt, fillcolor, pencolor):
        """
        Atomic shape used primarily for the hilt of the sword.
        _x, and _y are for coordinates
        height and width are used for the rectangle size
        tilt is for the direction that the rectangle is tilted or not.
        fillcolor is for the color inside of the circles
        pencolor is for the circle borders
        """
        _t.setheading(tilt)
        _t.up()
        _t.goto(_x, _y)
        _t.down()
        _t.color(pencolor, fillcolor)
        _t.begin_fill()
        for _i in range(2):
            _t.forward(width)
            _t.left(90)
            _t.forward(height)
            _t.left(90)

        _t.right(90)
        _t.end_fill()
        _t.up()

    def draw_line(self, _t, _x, _y, length, tilt):
        _t.setheading(tilt)
        _t.up()
        _t.goto(_x, _y)
        _t.down()
        _t.setheading(tilt)
        _t.forward(length)

class Wires:
    def line(self, _t, x, y, length, tilt):
        """
        draws the wires to the parachute.
        """
        _t.up()
        _t.goto(x,y)
        _t.down()
        _t.setheading(tilt)
        _t.forward(length)







def mistakes_count(mistakes):
        
    if mistakes == 0:        
        Wires.line("self", _t, 0, 0, 110, 30)
        Draw_shapes.draw_circle("self", _t, 95, 55, 60, 23, 180, "pink", "black")
        Wires.line("self", _t, 0, 0, 100, 55)
        Draw_shapes.draw_circle("self", _t, 55, 79, 75, 20, 180, "blue", "black")
        Wires.line("self", _t, 0, 0, 90, 80)
        Draw_shapes.draw_circle("self", _t, 15, 88, 95, 19, 180, "orange", "black")
        Wires.line("self", _t, 0, 0, 90, 105)
        Draw_shapes.draw_circle("self", _t, -24, 86, 105, 20, 180, "green", "black")
        Wires.line("self", _t, 0, 0, 100, 130)
        Draw_shapes.draw_circle("self", _t, -64, 75, 130, 23, 180, "yellow", "black")
        Wires.line("self", _t, 0, 0, 110, 155)

        Draw_shapes.draw_circle("self", _t, 13, -4, 143, 21, 360, "purple", "black")
        Draw_shapes.draw_rectangle("self", _t, 10, -42, 40, 20, 180, "teal", "black")
        Draw_shapes.draw_line("self", _t, 10, -42, 50, -80)
        Draw_shapes.draw_line("self", _t, -10, -42, 50, -105)
        Draw_shapes.draw_line("self", _t, 10, -82, 50, -80)
        Draw_shapes.draw_line("self", _t, -10, -82, 50, -105)

    elif mistakes == 1:
        """
        Draws missing line.
        """
        Wires.line("self", _t, 0, 0, 100, 55)
        Draw_shapes.draw_circle("self", _t, 55, 79, 75, 20, 180, "blue", "black")
        Wires.line("self", _t, 0, 0, 90, 80)
        Draw_shapes.draw_circle("self", _t, 15, 88, 95, 19, 180, "orange", "black")
        Wires.line("self", _t, 0, 0, 90, 105)
        Draw_shapes.draw_circle("self", _t, -24, 86, 105, 20, 180, "green", "black")
        Wires.line("self", _t, 0, 0, 100, 130)
        Draw_shapes.draw_circle("self", _t, -64, 75, 130, 23, 180, "yellow", "black")
        Wires.line("self", _t, 0, 0, 110, 155)

        Draw_shapes.draw_circle("self", _t, 13, -4, 143, 21, 360, "purple", "black")
        Draw_shapes.draw_rectangle("self", _t, 10, -42, 40, 20, 180, "teal", "black")
        Draw_shapes.draw_line("self", _t, 10, -42, 50, -60)
        Draw_shapes.draw_line("self", _t, -10, -42, 50, -125)
        Draw_shapes.draw_line("self", _t, 10, -82, 50, -60)
        Draw_shapes.draw_line("self", _t, -10, -82, 50, -125)

    elif mistakes == 2:
        """
        Draw 2 missing lines.
        """
        Wires.line("self", _t, 0, 0, 90, 80)
        Draw_shapes.draw_circle("self", _t, 15, 88, 95, 19, 180, "orange", "black")
        Wires.line("self", _t, 0, 0, 90, 105)
        Draw_shapes.draw_circle("self", _t, -24, 86, 105, 20, 180, "green", "black")
        Wires.line("self", _t, 0, 0, 100, 130)
        Draw_shapes.draw_circle("self", _t, -64, 75, 130, 23, 180, "yellow", "black")
        Wires.line("self", _t, 0, 0, 110, 155)

        Draw_shapes.draw_circle("self", _t, 13, -4, 143, 21, 360, "purple", "black")
        Draw_shapes.draw_rectangle("self", _t, 10, -42, 40, 20, 180, "teal", "black")
        Draw_shapes.draw_line("self", _t, 10, -42, 50, -40)
        Draw_shapes.draw_line("self", _t, -10, -42, 50, -145)
        Draw_shapes.draw_line("self", _t, 10, -82, 50, -40)
        Draw_shapes.draw_line("self", _t, -10, -82, 50, -145)

    elif mistakes == 3:
        """
        Draws 3 missing lines
        """

        Wires.line("self", _t, 0, 0, 90, 105)
        Draw_shapes.draw_circle("self", _t, -24, 86, 105, 20, 180, "green", "black")
        Wires.line("self", _t, 0, 0, 100, 130)
        Draw_shapes.draw_circle("self", _t, -64, 75, 130, 23, 180, "yellow", "black")
        Wires.line("self", _t, 0, 0, 110, 155)

        Draw_shapes.draw_circle("self", _t, 13, -4, 143, 21, 360, "purple", "black")
        Draw_shapes.draw_rectangle("self", _t, 10, -42, 40, 20, 180, "teal", "black")
        Draw_shapes.draw_line("self", _t, 10, -42, 50, -20)
        Draw_shapes.draw_line("self", _t, -10, -42, 50, -165)
        Draw_shapes.draw_line("self", _t, 10, -82, 50, -20)
        Draw_shapes.draw_line("self", _t, -10, -82, 50, -165)

    elif mistakes == 4:


        Wires.line("self", _t, 0, 0, 100, 130)
        Draw_shapes.draw_circle("self", _t, -64, 75, 130, 23, 180, "yellow", "black")
        Wires.line("self", _t, 0, 0, 110, 155)

        Draw_shapes.draw_circle("self", _t, 13, -4, 143, 21, 360, "purple", "black")
        Draw_shapes.draw_rectangle("self", _t, 10, -42, 40, 20, 180, "teal", "black")
        Draw_shapes.draw_line("self", _t, 10, -42, 50, 0)
        Draw_shapes.draw_line("self", _t, -10, -42, 50, -185)
        Draw_shapes.draw_line("self", _t, 10, -82, 50, 0)
        Draw_shapes.draw_line("self", _t, -10, -82, 50, -185)

    elif mistakes == 5:


        Draw_shapes.draw_circle("self", _t, -100, 47, 130, 23, 180, "yellow", "black")
        Wires.line("self", _t, 0, 0, 110, 155)

        Draw_shapes.draw_circle("self", _t, 13, -4, 143, 21, 360, "purple", "black")
        Draw_shapes.draw_rectangle("self", _t, 10, -42, 40, 20, 180, "teal", "black")
        Draw_shapes.draw_line("self", _t, 10, -42, 50, 60)
        Draw_shapes.draw_line("self", _t, -10, -42, 50, -245)
        Draw_shapes.draw_line("self", _t, 10, -82, 50, 60)
        Draw_shapes.draw_line("self", _t, -10, -82, 50, -245)

    elif mistakes == 6:

        Draw_shapes.draw_line("self", _t, 10, -42, 50, 60)
        Draw_shapes.draw_line("self", _t, -10, -42, 50, -245)
        Draw_shapes.draw_line("self", _t, 10, -82, 50, 60)
        Draw_shapes.draw_line("self", _t, -10, -82, 50, -245)
