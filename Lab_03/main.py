import math
from square_generator import SquareGenerator, InvalidRangeException


# TASK 01
one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

one_to_ten_squares = [i * i for i in one_to_ten]

print(one_to_ten_squares)


# TASK 02
def squares_from_range(start, end):
    return [i * i for i in range(start, end)]


print(squares_from_range(1, 10))


# TASK 03
print(SquareGenerator(2, 11).squares_from_range())


# TASK 04
square_gen = SquareGenerator(1, 11)

print([math.sqrt(i) for i in square_gen.squares_from_range()])


# TASK 05
try:
    print(SquareGenerator(5, 1).squares_from_range())
except InvalidRangeException:
    print("InvalidRangeException was thrown.")
