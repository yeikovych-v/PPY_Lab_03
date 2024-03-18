class InvalidRangeException(Exception):
    pass


class SquareGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def squares_from_range(self):
        if self.end < self.start:
            raise InvalidRangeException("End of the range was less than start parameter.")
        return [i * i for i in range(self.start, self.end)]