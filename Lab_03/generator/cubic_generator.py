from Lab_03.generator.square_generator import SquareGenerator, InvalidRangeException


class CubicGenerator(SquareGenerator):
    def __init__(self, start, end):
        super().__init__(start, end)

    def cubes_from_range(self):
        if self.end < self.start:
            raise InvalidRangeException("End of the range was less than start parameter.")
        return [i * i * i for i in range(self.start, self.end + 1)]

    def squares_from_range(self):
        if self.end < self.start:
            raise InvalidRangeException("End of the range was less than start parameter.")
        return [i * i for i in range(self.start, self.end + 1)]
