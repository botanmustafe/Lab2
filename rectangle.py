class Rectangle:        # rectangle with center (x,y) width and height

    def __init__(self, x: float = 0.0, y: float = 0.0, width: float = 1.0, height: float = 1.0) -> None:
        if not isinstance(x, (int, float)):
            raise TypeError("x has to be a number or decimal")
        if not isinstance(y, (int, float)):
            raise TypeError("y has to be a number or decimal")
        if not isinstance(width, (int, float)):
            raise TypeError("width has to be a number or decimal")
        if not isinstance(height, (int, float)):
            raise TypeError("height has to be a number or decimal")
        if width <= 0 or height <= 0:
            raise ValueError("width and height has to be larger than 0")

        self._x: float = float(x)
        self._y: float = float(y)
        self._width: float = float(width)
        self._height: float = float(height)

    @property
    def x(self) -> float:  # rectangle x-coordinate (read-only)
        return self._x

    @property
    def y(self) -> float:  # rectangle y-coordinate (read-only)
        return self._y

    @property
    def width(self) -> float:  # rectangle width (read-only)
        return self._width

    @property
    def height(self) -> float:  # rectangle height (read-only)
        return self._height

    @property
    def area(self) -> float:        # width * height = area (read-only)
        return self._width * self._height

    @property
    def perimeter(self) -> float:       # perimeter = 2 * (width + height) (read-only)
        return 2 * (self._width + self._height)

    # moves the rectangles center with dx and dy (x-axis & y-axis)
    def translate(self, dx: float, dy: float) -> None:
        if not isinstance(dx, (int, float)):
            raise TypeError("dx has to be a number or decimal")
        if not isinstance(dy, (int, float)):
            raise TypeError("dy has to be a number or decimal")

        self._x += dx
        self._y += dy

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):            # equal if the sizes match
            return False
        return {self._width, self._height} == {other._width, other._height}

    # get area from "other" if it exists
    def other_area(self, other):
        return other.area if hasattr(other, "area") else NotImplemented

    def __lt__(self, other) -> bool:   # true if the rectangles area is smaller than the other ones
        oa = self.other_area(other)
        if oa is NotImplemented:
            return NotImplemented
        return self.area < oa

    # true if the rectangles area is smaller than or equal to the other ones
    def __le__(self, other) -> bool:
        oa = self.other_area(other)
        if oa is NotImplemented:
            return NotImplemented
        return self.area <= oa

    def __gt__(self, other) -> bool:    # true if the rectangles area is larger than the other ones
        oa = self.other_area(other)
        if oa is NotImplemented:
            return NotImplemented
        return self.area > oa

    # true if the rectangles area is larger than or equal to the other ones
    def __ge__(self, other) -> bool:
        oa = self.other_area(other)
        if oa is NotImplemented:
            return NotImplemented
        return self.area >= oa

    # textrepresentation

    def __repr__(self) -> str:
        return f"Rectangle(x={self._x}, y={self._y}, width={self._width}, height={self._height})"

    def __str__(self) -> str:
        return f"Rectangle at ({self._x}, {self._y}) with width={self._width} and height={self._height}"

    def is_square(self) -> bool:
        return self._width == self._height
