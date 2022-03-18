from graphics import Circle, GraphWin, Point, Text
import math


def add_ten(nums):
    acc = 0
    for i in nums:
        i += 10
        nums[acc] = i
        acc +=1


def square_each(nums):
    acc = 0
    for i in nums:
        i = i ** 2
        nums[acc] = i
        acc += 1
    return nums


def sum_list(nums):
    acc = 0
    for x in nums:
        if type(x) == float:
            for i in nums:
                acc = float(acc + i)
            return acc
    for i in nums:
        acc = acc + i
    return acc


def to_numbers(nums):
    acc = 0
    for i in nums:
        try:
            i = int(i)
            nums[acc] = i
            acc += 1
        except ValueError:
            i = float(i)
            nums[acc] = i
            acc += 1




def sum_of_squares(nums):
    # print(nums)
    acc = 0
    for x in nums:
        ch = '.'
        try:
            x = x.split(",")
            print(x)
            acc2 = 0
            print(x)
            for i in x:
                # print(i)
                if ch in i:
                    i = float(i)
                    x[acc2] = i
                    acc2 += 1
                    # print(i)
                else:
                    i = int(i)
                    x[acc2] = i
                    acc2 += 1
            acc2 = 0
            for i in x:
                i = i ** 2
                x[acc2] = i
                acc2 += 1
            x = sum_list(x)
            nums[acc] = x
        except AttributeError:
            if ch in x:
                x = float(x)
            else:
                x = int(x)
            x = x ** 2
            nums[acc] = x
        acc += 1

    return nums
    # Could have just used the functions... not sure why that only occurs to me after i'm waaaaay too far to go back xD
    # went back


def starter(weight, wins):
    if ((weight < 160) and (weight >= 150)) and (wins >= 5):
        return True
    elif (weight > 199) or (wins > 20):
        return True
    else:
        return False


def leap_year(year):
    if ((year%4) == 0) and ((year % 100) != 0) or ((year %400) == 0):
        return True
    else:
        return False



def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("red")
    circle_two.draw(win)
    if did_overlap(circle_one,circle_two) == True:
        text = Text(Point(5,8), "The circles overlap.")

        text.draw(win)
    elif did_overlap(circle_one,circle_two) == False:
        text = Text(Point(5,8), "The circles do not overlap.")

        text.draw(win)



    win.getMouse()
    win.close()

def did_overlap(circle_one, circle_two):
    p1 = circle_one.getCenter()
    p2 = circle_two.getCenter()
    d = math.sqrt(((p2.getX() - p1.getX()) ** 2) + ((p2.getY() - p1.getY()) ** 2))
    print(d)
    print(circle_one.getRadius())
    radi = circle_one.getRadius() + circle_two.getRadius()
    radi2 = abs(circle_one.getRadius() - circle_two.getRadius())
    print(radi)
    print(radi2)
    if d >= radi2 and d <= radi:
        print('hi')
        return True
    else:
        print('no')
        return False



if __name__ == '__main__':
    pass
