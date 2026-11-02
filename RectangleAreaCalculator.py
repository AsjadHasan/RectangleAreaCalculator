"""Calculate the area of multiple rectangles."""


class Rectangle:
    """Represent a rectangle with width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle's width and height."""
        self.width = width
        self.height = height

    def get_area(self):
        """Calculate and print the rectangle's area."""
        area = self.width * self.height
        print(f"Rectangle area: {area}")


# Create two Rectangle objects
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 4)


# Call the method for both objects
rectangle1.get_area()
rectangle2.get_area()