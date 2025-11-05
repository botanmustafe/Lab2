from math import pi  # i use pi to count area and perimiter


class Circle:  # class circle

    # creating the circle with a specific position on the table

    def __init__(self, x=0.0, y=0.0, radius=1.0):

        # i use isinstance to make sure the user enters valid numbers (not letters or other types)

        if not isinstance(x, (int, float)):
            raise TypeError("x has to be a number,")
        if not isinstance(y, (int, float)):
            raise TypeError("y has to be a number")
        if not isinstance(radius, (int, float)):
            raise TypeError("radius has to be a number")
        if radius <= 0:
            raise ValueError("radius måste vara större än 0")

        # i save the value with underscore, making it private

        self._x = float(x)
        self._y = float(y)
        self._radius = float(radius)

        # these properties makes the right calculations, (read-only) (unchangeable)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return pi * (self._radius ** 2)

    @property
    def perimeter(self):
        return 2 * pi * self._radius

    # methods
    # this translate method moves the x and y, dx (how much to )

    def translate(self, dx, dy):
        if not isinstance(dx, (int, float)):
            raise TypeError("dx måste vara ett tal")
        if not isinstance(dy, (int, float)):
            raise TypeError("dy måste vara ett tal")

        # move the centrum
        self._x += dx
        self._y += dy

    # returnerar True om cirkeln är en cirkel (radius = 1)

    def is_unit_circle(self):
        return self._radius == 1.0

    # comparisons with "dunder methods" (these comparisons are unchangeable)




    def __eq__(self, other):    # check if two circles have the same size
        if not isinstance(other, Circle):
            return False
        return self._radius == other._radius

    def __lt__(self, other):    # compares area, true if the circle is smaller than another
        if not isinstance(other, Circle):
            return NotImplemented
        return self.area < other.area

    def __le__(self, other):                # checks if the circle is smaller or equal to another
        if not isinstance(other, Circle):
            return NotImplemented
        return self.area <= other.area

    def __gt__(self, other):
        if not isinstance(other, Circle):   # checks if the circle is bigger then another
            return NotImplemented
        return self.area > other.area

    def __ge__(self, other):
        if not isinstance(other, Circle): # checks if the circle is bigger or equal then another
            return NotImplemented
        return self.area >= other.area

    # textrepresentation

    def __repr__(self):
        return f"Circle(x={self._x}, y={self._y}, radius={self._radius})"

    
    def __str__(self):
        return f"Circle at ({self._x}, {self._y}) with radius {self._radius}"
