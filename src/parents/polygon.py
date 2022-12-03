#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Polygon(metaclass=ABCMeta):
    NAME = None

    def __init__(self, count_side, size_side=list, angles=list):
        self.count_side = count_side
        self.size_side = size_side
        self.angles = angles

    @property
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def add_area(self, figure):
        if figure.area < 0 or not issubclass(figure, Polygon):
            raise ValueError('the values transmitted do not correspond to')
        return self.area + figure.area

    @abstractmethod
    def sum_angles_triangle(self):
        pass


if __name__ == "__main__":
    pass
