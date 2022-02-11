"""Name: Joshua Bee son
<hw1.py>
Problem:f This program solves the issue of having to manually calculate several simple equations.
I certify that this assignment is entirely my own work."""
from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for i in range(num_clicks):
        click = win.getMouse()


        # move amount is distance from center of square to the
        # point where the user clicked
        change_x = click.getX()
        change_y = click.getY()
        new_shape = Rectangle(Point(change_x + 25, change_y + 25), Point(change_x -25, change_y - 25))
        new_shape.setOutline("red")
        new_shape.setFill("red")
        new_shape.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)
    font_size = 12
    #what I need, one rectangle object and 3 text boxes
    prompt = Text(Point(200,20), "Click twice at two opposite corners to create a rectangle")
    prompt.setSize(font_size)
    prompt.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()

    shape = Rectangle(Point(p1.getX(),p1.getY()),Point(p2.getX(),p2.getY()))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    a = abs((p1.getX() - p2.getX()) * (p1.getY() - p2.getY()))
    p = abs(((p1.getX() - p2.getX()) * 2) + ((p1.getY() - p2.getY()) * 2))
    print(a,p)


    perimeter = Text(Point(200,350), "Perimeter: ")
    info_per = perimeter.clone()
    info_per.move(100,0)
    info_per.setText(p)
    info_per.draw(win)
    perimeter.draw(win)


    area = Text(Point(200,375), "Area: ")
    info_area = area.clone()
    info_area.move(100,0)
    info_area.setText(a)
    info_area.draw(win)
    area.draw(win)

    win.getMouse()
    win.close()
    pass


def circle():
    pass


def pi2():
    pass


if __name__ == '__main__':
    pass