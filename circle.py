from math import pi  # i use pi to count area and perimiter


# a circle with center (x, y) and radius, area and perimeter can be read but not changed. Supports comparisons
class Circle:

    def __init__(self, x: float = 0.0, y: float = 0.0, radius: float = 1.0) -> None:

        # i use isinstance to make sure the user enters valid numbers (not letters or other types)

        if not isinstance(x, (int, float)):
            raise TypeError("x has to be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y has to be a number")
        if not isinstance(radius, (int, float)):
            raise TypeError("radius has to be a number")
        if radius <= 0:
            raise ValueError("radius has to be bigger then 0")

        # i save the value with underscore, making it private

        self._x: float = float(x)
        self._y: float = float(y)
        self._radius: float = float(radius)

        # these properties makes the right calculations, (read-only) (unchangeable)

    @property
    def x(self) -> float:   # circles x-koordinat (read-only)
        return self._x

    @property
    def y(self) -> float:   # circles y-koordinat (read-only)
        return self._y

    @property
    def radius(self) -> float:  # circles radius (read-only)
        return self._radius

    @property
    def area(self) -> float:
        return pi * (self._radius ** 2)     # area = π * r^2 (read-only)

    @property
    def perimeter(self) -> float:
        return 2 * pi * self._radius    # perimeter = 2 * π * r (read-only)

    # methods
    # moves the circles center with dx and dy (x-axis, y-axis)

    def translate(self, dx: float, dy: float) -> None:
        if not isinstance(dx, (int, float)):
            raise TypeError("dx has to be a number or decimal")
        if not isinstance(dy, (int, float)):
            raise TypeError("dy has to be a number or decimal")

        # move the centrum
        self._x += dx
        self._y += dy

    # returns true if radius is 1.0

    def is_unit_circle(self) -> bool:
        return self._radius == 1.0

    # comparisons with "dunder methods" (these comparisons are unchangeable)

    def __eq__(self, other) -> bool:    # check if two circles have the same size
        if not isinstance(other, Circle):
            return False
        return self._radius == other._radius

    def __lt__(self, other) -> bool:    # compares area, true if the circle is smaller than another
        if not isinstance(other, Circle):
            return NotImplemented
        return self.area < other.area

    # checks if the circle is smaller or equal to another
    def __le__(self, other) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.area <= other.area

    def __gt__(self, other) -> bool:
        if not isinstance(other, Circle):   # checks if the circle is bigger then another
            return NotImplemented
        return self.area > other.area

    def __ge__(self, other) -> bool:
        # checks if the circle is bigger or equal then another
        if not isinstance(other, Circle):
            return NotImplemented
        return self.area >= other.area

    # textrepresentation

    def __repr__(self) -> str:
        return f"Circle(x={self._x}, y={self._y}, radius={self._radius})"

    def __str__(self) -> str:
        return f"Circle at ({self._x}, {self._y}) with radius {self._radius}"
