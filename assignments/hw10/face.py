from graphics import Circle, Line, Point


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.size = size
        self.center = center
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        eye_size = 0.15 * self.size
        eye_off = self.size / 3.0
        mouth_size = 0.8 * self.size
        mouth_off = self.size / 2.0
        self.head = Circle(self.center, self.size)
        self.head.draw(self.window)
        self.left_eye = Circle(self.center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(self.center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(self.window)
        self.right_eye.draw(self.window)
        point_1 = self.center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = self.center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(self.window)
        point_3 = self.center.clone()
        point_3.move(0, (mouth_off + (mouth_off / 2)))
        self.one = Line(point_1, point_3)
        self.one.draw(self.window)
        self.two = Line(point_2, point_3)
        self.two.draw(self.window)

        pass

    def shock(self):
        eye_size = 0.15 * self.size
        eye_off = self.size / 3.0
        mouth_size = 0.8 * self.size
        mouth_off = self.size / 2.0
        self.head = Circle(self.center, self.size)
        self.head.draw(self.window)
        self.left_eye = Circle(self.center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(self.center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(self.window)
        self.right_eye.draw(self.window)
        point_1 = self.center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = self.center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        point_3 = self.center.clone()
        point_3.move(0, (mouth_off + (mouth_off / 2)))
        circle = Circle(point_3, eye_size)
        circle.draw(self.window)

        pass

    def wink(self):
        eye_size = 0.15 * self.size
        eye_off = self.size / 3.0
        mouth_size = 0.8 * self.size
        mouth_off = self.size / 2.0
        self.head = Circle(self.center, self.size)
        self.head.draw(self.window)
        point_3 = Point((self.center / 2), self.right_eye.getCenter().getY())
        point_4 = Point((-(self.center / 2)), self.right_eye.getCenter().getY())
        self.left_eye = Line(point_4,point_3)
        self.left_eye.draw(self.window)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(self.center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(self.window)
        self.right_eye.draw(self.window)
        point_1 = self.center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = self.center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(self.window)
        point_3 = self.center.clone()
        point_3.move(0, (mouth_off + (mouth_off / 2)))
        self.one = Line(point_1, point_3)
        self.one.draw(self.window)
        self.two = Line(point_2, point_3)
        self.two.draw(self.window)

        pass
