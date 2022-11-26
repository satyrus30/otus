#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.parents.polygon import *
from collections import Counter


class Rectangle(Polygon):
    NAME = 'rectangle'

    def calculate_area(self):
        a, b = self.size_side
        area = a * b
        return round(area)

    def calculate_perimeter(self):
        a, b = self.size_side
        return 2 * (a + b)

    def add_area(self, figure):
        return self.calculate_area() + figure

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
        и summ == 4
        :param list_val: Список длин сторон прямоугольника
        :return:
        number_of_pairs: количество пар Counter({10: 2, 20: 2})
        sum_values: сумма значений (side_1: 2,side_1: 2)
        """
        sum_values = sum(Counter(list_val).values())
        number_of_pairs = len(Counter(list_val))
        return number_of_pairs, sum_values


if __name__ == "__main__":
    pass
