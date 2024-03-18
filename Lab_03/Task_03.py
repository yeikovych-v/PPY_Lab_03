class SquareGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def squares_from_range(self):
        return [i * i for i in range(self.start, self.end)]


print(SquareGenerator(2, 11).squares_from_range())
