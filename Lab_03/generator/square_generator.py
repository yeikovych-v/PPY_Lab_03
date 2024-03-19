from abc import ABC, abstractmethod


class InvalidRangeException(Exception):
    pass


class SquareGenerator(ABC):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @abstractmethod
    def squares_from_range(self):
        pass

