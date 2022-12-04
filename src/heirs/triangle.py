#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.parents.polygon import *
from collections import Counter


class Triangle(Polygon):
    NAME = 'triangle'

    @property
    def area(self):
        a, b, c = self.size_side
        half_perimetr = self.perimeter/2
        area = (half_perimetr * abs(half_perimetr - a) * abs(half_perimetr - b) * abs(half_perimetr - c)) ** 0.5
        return round(area)

    @property
    def perimeter(self):
        return sum(self.size_side)

    def add_area(self, figure):
        return self.area + figure.area

    def check_value(self):
        return self.count_side, self.size_side, self.angles

    @staticmethod
    def check_less_than_zero(list_val):
        return [i for i in list_val if i <= 0]

    def sum_angles_triangle(self):
        return sum(self.angles)

    @staticmethod
    def check_repeating_elem(list_val):
        """
        В прямоугольнике 2 пары сторон с одинаковыми длинами [10, 20, 10, 20] -> (side_1: 2,side_1: 2) -> len() == 2
        :param list_val: Список длин сторон прямоугольника
        :return:
        number_of_pairs: количество пар Counter({10: 2, 20: 2})
        """
        number_of_pairs = len(Counter(list_val))
        return number_of_pairs


if __name__ == "__main__":
    pass
