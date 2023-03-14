class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

rectangle = Rectangle("Rectangle 1", 5, 10)

rectangle_area = rectangle.area()

print("The area of the rectangle is:", rectangle_area)

circle = Circle("Circle 1", 4)

circle_area = circle.area()

print("The area of the circle is:", circle_area)
