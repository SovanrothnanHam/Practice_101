'''
Ex4
Exercise: Creating a Simple Class

Create a Python class called `Rectangle` to represent a rectangle. The `Rectangle` class should have the following attributes and methods:

Attributes:
- `width`: A floating-point number representing the width of the rectangle.
- `height`: A floating-point number representing the height of the rectangle.

Methods:
- `__init__(self, width, height)`: The constructor method to initialize the `width` and `height` attributes.
- `get_area(self)`: A method that returns the area of the rectangle (width * height).
- `get_perimeter(self)`: A method that returns the perimeter of the rectangle (2 * (width + height)).

Write the `Rectangle` class with the provided attributes and methods and test it using sample data.

Example Usage:


# Create a rectangle object with width=5 and height=3
rect = Rectangle(5, 3)

# Get the area of the rectangle
area = rect.get_area()
print(area)  # Output: 15

# Get the perimeter of the rectangle
perimeter = rect.get_perimeter()
print(perimeter)  # Output: 16


'''


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
