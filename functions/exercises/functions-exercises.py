# Part 1 A -- Make a Line
# def make_line(Size):
#     return '#'* Size
# print(make_line(5))
    


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
# def make_line(Size):
#     return '#'* Size
# def make_square(size):
#     return '\n'.join(make_line(size) for _ in range(size))
# print(make_square(2))



# # Part 1 C -- Make a Rectangle
# def make_line(Size):
#     return '#'* Size
# def make_rectangle(size):
#     return '\n'.join(make_line(size) for _ in range(size))
# print(make_rectangle(7))



# Part 2 A -- Make a Stairs
# def make_stairs(size):
#     return '\n'.join('#' * i + ' ' * (size - i - 1) for i in range(size))
# print(make_stairs(8))


# Part 2 B -- Make Space-Line 
# def make_space_line(size):
#     return '\n'.join('#' * i + ' ' * (size - i) for i in range(size))
# print(make_space_line(8))



# Part 2 C -- Make Isosceles Triangle
# def make_isosceles_triangle(size):
#     return '\n'.join(('#' * (2 * i + 1)).center(2 * size - 1) for i in range(size))
# print(make_isosceles_triangle(5))


# Part 3 -- Make a Diamond
def make_diamond(size):
    if size <= 0:
        return ""  
    top_part = '\n'.join(('#' * (2 * i + 1)).center(2 * size - 1) for i in range(size))
    bottom_part = '\n'.join(('#' * (2 * i + 1)).center(2 * size - 1) for i in range(size - 2, -1, -1))
    return top_part + '\n' + bottom_part
print(make_diamond(5))






