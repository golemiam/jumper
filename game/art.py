import turtle
    
_t = turtle.Turtle()

class draw_shapes:
    def draw_circle(_t, _x, _y, radius, extent, fillcolor, pencolor):
        """
        This is the atomic shape circle used for the ball on the sword and the shield in various places throughout.
        _x, and _y are for coordinates
        radius is used for the circle size
        fillcolor is for the color inside of the circles
        pencolor is for the circle borders
        """
        _t.color(pencolor, fillcolor)
        _t.begin_fill()
        _t.up()
        _t.goto(_x,_y)
        _t.down()
        _t.circle(radius, extent)
        _t.end_fill()
        _t.speed(0)

    def draw_rectangle(_t, _x, _y, height, width, tilt, fillcolor, pencolor):
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

    def draw_line(_t, _x, _y, length):
        _t.setheading(tilt)
        _t.up()
        _t.goto(_x, _y)
        _t.down()
        _t.forward(length)
        
class Full_image:
    def __init__(self):
        self.wires = Wires()
        self.person = Person()
        self.chute = Chute()

    def draw_image(self):
        Wires()
        Person()
        Chute()

class Chute:
    """
    draws the parachute top
    """
    def half_circle(self):
        """
        draws the half circles used to make the parachute.
        """
        draw_circle(_t, _x, _y, radius, extent, fillcolor, pencolor)
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

class Person:
    def __init__(self):
        self.circle = draw_circle()
    def head():
        """
        """
    def arm(self):
        """
        """
    def leg(self):
        """
        """






        
        
Wires.line("self", _t, 0, 0, 110, 30)
Wires.line("self", _t, 0, 0, 100, 55)
Wires.line("self", _t, 0, 0, 90, 80)
Wires.line("self", _t, 0, 0, 90, 105)
Wires.line("self", _t, 0, 0, 100, 130)
Wires.line("self", _t, 0, 0, 110, 155)

