import math
from Lab_03.generator.square_generator import SquareGenerator, InvalidRangeException
from Lab_03.generator.cubic_generator import CubicGenerator


# TASK 01
print("TASK 01:")
one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

one_to_ten_squares = [i * i for i in one_to_ten]

print(one_to_ten_squares)


# TASK 02
print("TASK 02:")


def squares_from_range(start, end):
    return [i * i for i in range(start, end)]


print(squares_from_range(1, 10))


# TASK 03
print("TASK 03:")
# print(SquareGenerator(2, 11).squares_from_range())


# TASK 04
print("TASK 04:")
# square_gen = SquareGenerator(1, 11)

# print([math.sqrt(i) for i in square_gen.squares_from_range()])


# TASK 05
print("TASK 05:")
# try:
#     print(SquareGenerator(5, 1).squares_from_range())
# except InvalidRangeException:
#     print("InvalidRangeException was thrown.")


# TASK 08
print("TASK 08:")
print(CubicGenerator(2, 11).cubes_from_range())


# TASK 09
print("TASK 09:")
try:
    print(CubicGenerator(5, 1).squares_from_range())
except InvalidRangeException:
    print("InvalidRangeException was thrown.")


# TASK 10
print("TASK 10:")
print(CubicGenerator(5, 11).squares_from_range())
