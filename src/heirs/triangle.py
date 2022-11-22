#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.parents.polygon import *
from collections import Counter


class Triangle(Polygon):
    NAME = 'triangle'

    def calculate_area(self):
        a, b, c = self.size_side
        half_perimetr = self.calculate_perimeter()/2
        area = (half_perimetr * abs(half_perimetr - a) * abs(half_perimetr - b) * abs(half_perimetr - c)) ** 0.5
        return round(area)

    def calculate_perimeter(self):
        return sum(self.size_side)

    def add_area(self, figure):
        return self.calculate_area() + figure

    def check_count_side(self):
        return self.count_side

    @staticmethod
    def check_count_elem(list_val):
        return len(list_val)

    @staticmethod
    def check_is_not_zero(list_val):
        return len([i for i in list_val if i == 0])

    @staticmethod
    def check_is_num(list_val):
        return len([i for i in list_val if type(i) == str])

    @staticmethod
    def check_less_than_zero(list_val):
        return len([i for i in list_val if i < 0])

    def sum_angles_triangle(self):
        return sum(self.angles)

    @staticmethod
    def check_repeating_elem(list_val):
        return len(Counter(list_val))


if __name__ == "__main__":
    pass
