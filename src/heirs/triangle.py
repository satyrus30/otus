#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.parents.polygon import *


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

    def get_max_side(self):
        return max(self.size_side)




if __name__ == "__main__":
    tr = Triangle(3, [1,10,10])
    print(tr.add_area(5))
