#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.parents.polygon import *


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


if __name__ == "__main__":
    pass
