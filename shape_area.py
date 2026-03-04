# https://quera.org/problemset/33473?tab=description
# --------------------------------------------------
# further possible improvement: create a factory method which return a relevant class based on shape type input
# where each shape class follows an abstraction that enforces implementation of area and perimeter calculation methods

from math import pi


def square_area(a):
    return a**2


def circle_area(r):
    return pi * r**2


def rectangle_area(a, b):
    return a * b


def triangle_area(h, b):
    return h * b / 2


AREA_MAPPER = {
    "square": square_area,
    "circle": circle_area,
    "rectangle": rectangle_area,
    "triangle": triangle_area,
}


def get_func(ls):
    return [AREA_MAPPER[shape] for shape in ls]
