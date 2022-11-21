#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.parents.ball import *


class Circle(Ball):
    NAME = 'circle'

    def calculate_area(self):
        return round(self.p * self.size_radius ** 2)

    def calculate_perimeter(self):
        return Ball.calculate_perimeter(self)

    def add_area(self, figure):
        return Ball.add_area(self, figure)


if __name__ == "__main__":
    pass
