#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.heirs.triangle import *
import pytest

MAX_COUNT_TRIANGLE = 3
SUM_ANGLES = 180


def test_correct_count_side():
    correct_count_side = Triangle(3, [10.5, 40, 50], [121, 30, 30])
    message = f"""Number of sides - {correct_count_side.count_side}, the figure is not a triangle"""
    assert correct_count_side.count_side == MAX_COUNT_TRIANGLE, message


@pytest.mark.negative
@pytest.mark.parametrize('incorrect_count_side', [Triangle(4, [10, 10.5, 50], [100, 66.5, 20]),
                                                  Triangle('3', [10, 10.5, 50], [100, 66.5, 20])])
def test_incorrect_count_side(incorrect_count_side):
    message = f"""Number of sides - {incorrect_count_side.count_side}, the figure is not a triangle"""
    assert incorrect_count_side.count_side == MAX_COUNT_TRIANGLE, message


def test_correct_size_side():
    correct_size_side = Triangle(3, [10, 60, 65], [120, 30, 33])
    max_size = max(correct_size_side.size_side)
    other_parties = sum(correct_size_side.size_side) - max_size
    message = 'The sum of the lengths of the two sides of the triangle is less than the length of the remaining side'
    assert other_parties > max_size, message


@pytest.mark.negative
@pytest.mark.parametrize('count_size_site', [Triangle(3, [10, 60], [120, 30, 33]),
                                             Triangle(3, [10, 60, 20, 40], [120, 30, 33])])
def test_count_elem_size_site(count_size_site):
    message = "Number of side dimensions less than or greater than 3"
    assert count_size_site.check_count_elem(count_size_site.size_side) == MAX_COUNT_TRIANGLE, message


@pytest.mark.negative
def test_size_side_is_zero():
    size_side_is_zero = Triangle(0, [0, 60, 50], [9, 0, 30])
    message = "One of the sides is zero"
    assert size_side_is_zero.check_is_not_zero(size_side_is_zero.size_side) == 0, message


@pytest.mark.negative
def test_size_side_is_not_num():
    size_side_not_num = Triangle(0, [20, 60, '50'], [9, 0, 30])
    message = "One of the sides is not number"
    assert size_side_not_num.check_is_num(size_side_not_num.size_side) == 0, message


@pytest.mark.negative
def test_size_side_less_than_zero():
    less_than_zero = Triangle('a', [-10, 0, 50], [-20, 180, 20])
    message = "One of the angles less than zero"
    assert less_than_zero.check_less_than_zero(less_than_zero.size_side) == 0, message


def test_correct_angles():
    correct_angles = Triangle(3, [10, -10, 50], [80, 40, 60])
    message = "The size of the angles in the triangle is not correct"
    assert correct_angles.sum_angles_triangle() == SUM_ANGLES, message


@pytest.mark.negative
def test_angle_is_zero():
    angle_is_zero = Triangle('a', [10, 0, 50], [0, 150, 30])
    message = "The size of the angle in the triangle equal 0"
    assert angle_is_zero.check_is_not_zero(angle_is_zero.angles) == 0, message


@pytest.mark.negative
def test_angle_is_not_num():
    angle_is_not_num = Triangle('a', [10, 0, 50], [20, '125', 35])
    message = "One of the angles is not number"
    assert angle_is_not_num.check_is_num(angle_is_not_num.angles) == 0, message


@pytest.mark.negative
def test_angle_less_than_zero():
    less_than_zero = Triangle('a', [10, 0, 50], [-20, 180, 20])
    message = "One of the angles less than zero"
    assert less_than_zero.check_less_than_zero(less_than_zero.angles) == 0, message


@pytest.mark.negative
@pytest.mark.parametrize('count_angle', [Triangle(3, [30, 60, 40], [120, 30]),
                                         Triangle(3, [30, 60, 40], [120, 30, 33, 44])])
def test_count_elem_angle(count_angle):
    message = "Number of angle dimensions less than or greater than 3"
    assert count_angle.check_count_elem(count_angle.angles) == MAX_COUNT_TRIANGLE, message


def test_isosceles_triangle_by_sides():
    isosceles_triangle = Triangle(3, [60, 60, 10], [85.22, 85.22, 9.66])
    message = "The number of sides in an isosceles triangle is less than or greater than 2"
    assert isosceles_triangle.check_repeating_elem(isosceles_triangle.size_side) == 2, message


def test_isosceles_triangle_by_angles():
    isosceles_triangle = Triangle(3, [60, 60, 10], [85.22, 85.22, 9.66])
    message = "The number of angles in an isosceles triangle is less than or greater than 2"
    assert isosceles_triangle.check_repeating_elem(isosceles_triangle.angles) == 2, message


def test_equilateral_triangle_by_sides():
    equilateral_triangle = Triangle(3, [60, 60, 60], [60, 60, 60])
    message = "The number of sides in an isosceles triangle is less than or greater than 2"
    assert equilateral_triangle.check_repeating_elem(equilateral_triangle.size_side) == 1, message


def test_equilateral_triangle_by_angles():
    equilateral_triangle = Triangle(3, [60, 60, 60], [60, 60, 60])
    message = "The number of angles in an isosceles triangle is less than or greater than 2"
    assert equilateral_triangle.check_repeating_elem(equilateral_triangle.angles) == 1, message
