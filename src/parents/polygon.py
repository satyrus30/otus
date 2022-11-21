#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Polygon:
    NAME = None

    def __init__(self, count_side, size_side=list):
        if len(size_side) != count_side:
            raise ValueError("The length is not given for all sides")
        if count_side < 3:
            raise ValueError("The number of sides doesn't match the polygon")
        self.count_side = count_side
        self.size_side = size_side

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        return sum(self.size_side)

    def add_area(self, figure):
        pass


if __name__ == "__main__":
    pass
