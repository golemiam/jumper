import turtle

class Full_image:
    def __init__():
        self.wires = Wires()
        self.person = Person()
        self.chute = Chute()

    def draw_image():
        Wires()
        Person()
        Chute()
        def draw_circle(_t, _x, _y, radius, fillcolor, pencolor):
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
            _t.circle(radius)
            _t.end_fill()
            _t.speed(0)

class Wires:
    def line():
        """
        """

class Person:
    def __init__():
        self.circle = draw_circle()
    def head():
        """
        """
    def arm():
        """
        """
    def leg():
        """
        """

class Chute:
    """
    """
    def half_circle():
        """
        """

person()

class draw_shapes:
    def draw_circle(_t, _x, _y, radius, fillcolor, pencolor):
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
        _t.circle(radius)
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