#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Ball(metaclass=ABCMeta):
    NAME = 'ball'

    def __init__(self, size_radius, diameter):
        self.size_radius = size_radius
        self.diameter = diameter
        self.p = 3.14

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
    def check_diameter(self):
        pass
