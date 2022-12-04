#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.parents.ball import *



class Circle(Ball):
    NAME = 'circle'

    def calculate_area(self):
        return round(self.p * self.size_radius ** 2)

    def calculate_perimeter(self):
        return round(2 * self.p * self.size_radius)

    def add_area(self, figure):
        return self.calculate_perimeter() + figure

    def check_diameter(self):
        diameter = 2 * self.size_radius
        return diameter

    def check_value_type(self):
        return type(self.size_radius), type(self.diameter)

    def get_value(self):
        return self.size_radius, self.diameter


if __name__ == "__main__":
    pass
