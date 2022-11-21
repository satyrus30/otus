#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.heirs.rectangle import *


class Square(Rectangle):
    NAME = 'square'

    def calculate_area(self):
        a = self.size_side
        area = a ** 2
        return round(area)

    def calculate_perimeter(self):
        a = self.size_side
        return 4 * a

    def add_area(self, figure):
        return self.calculate_area() + figure


if __name__ == "__main__":
    pass