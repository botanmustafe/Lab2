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
