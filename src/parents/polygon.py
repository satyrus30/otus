#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Polygon(metaclass=ABCMeta):
    NAME = None

    def __init__(self, count_side, size_side=list, angles=list):
        self.count_side = count_side
        self.size_side = size_side
        self.angles = angles

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def add_area(self, figure):
        pass

    @abstractmethod
    def sum_angles_triangle(self):
        pass


if __name__ == "__main__":
    pass
