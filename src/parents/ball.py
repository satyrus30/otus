#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Ball:
    NAME = 'ball'

    def __init__(self, size_radius):
        self.size_radius = size_radius
        self.p = 3.14

    def calculate_area(self):
        return round(4 * self.p * self.size_radius ** 2)

    def calculate_perimeter(self):
        return round(2 * self.p * self.size_radius)

    def add_area(self, figure):
        return self.calculate_perimeter() + figure
