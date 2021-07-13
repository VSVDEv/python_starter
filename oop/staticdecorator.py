class MyObject:
    atr = 8

    def __init__(self):
        self.data_atr = 40

    def instance_method(self):
        return self.data_atr

    @staticmethod
    def static_method():
        print(MyObject.atr)


# if our module run as running file

if __name__ == "__main__":
    MyObject.static_method()
    obj = MyObject()
    obj.instance_method()
    obj.static_method()


class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    # return string of object
    def __repr__(self):
        return "Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return "Circle(%.1f)" % self.radius

    @classmethod
    def from_rect(cls, rectangle):
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return cls(radius)


def main():
    rectangle = Rectangle(3, 4)
    print(rectangle)

    first_circle = Circle(1)
    print(first_circle)


if __name__ == "__main__":
    main()

# second_circle = Circle.from_rect(rectangle)
# print(second_circle)
