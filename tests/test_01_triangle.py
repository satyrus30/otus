#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.heirs.triangle import *
import pytest

MAX_COUNT_TRIANGLE = 3
SUM_ANGLES = 180


@pytest.mark.positive_triangle
def test_correct_count_side():
    correct_count_side = Triangle(3, [10.5, 40, 50], [121, 30, 30])
    message = f"""Number of sides - {correct_count_side.count_side}, the figure is not a triangle"""
    assert correct_count_side.count_side == MAX_COUNT_TRIANGLE, message


@pytest.mark.negative_triangle
@pytest.mark.parametrize('incorrect_count_side, max_count', [
    (Triangle(2, [10, 10.5, 50], [100, 66.5, 20]), MAX_COUNT_TRIANGLE),
    (Triangle('4', [10, 10.5, 50], [100, 66.5, 20]), MAX_COUNT_TRIANGLE)])
def test_incorrect_count_side(incorrect_count_side, max_count):
    message = f"""Number of sides - {incorrect_count_side.count_side}, the figure is not a triangle"""
    assert incorrect_count_side.count_side != max_count, message


@pytest.mark.positive_triangle
def test_correct_size_side():
    correct_size_side = Triangle(3, [10, 60, 65], [120, 30, 33])
    max_size = max(correct_size_side.size_side)
    other_parties = sum(correct_size_side.size_side) - max_size
    message = 'The sum of the lengths of the two sides of the triangle is less than the length of the remaining side'
    assert other_parties > max_size, message


@pytest.mark.negative_triangle
@pytest.mark.parametrize('count_size_site, max_count', [
    (Triangle(3, [10, 60], [120, 30, 33]), MAX_COUNT_TRIANGLE),
    (Triangle(3, [10, 60, 20, 40], [120, 30, 33]), MAX_COUNT_TRIANGLE)])
def test_count_elem_size_site(count_size_site, max_count):
    message = f"Number of side dimensions less than or greater than {max_count}"
    assert count_size_site.check_count_elem(count_size_site.size_side) != max_count, message


@pytest.mark.negative_triangle
def test_size_side_is_zero():
    size_side_is_zero = Triangle(0, [0, 60, 50], [9, 0, 30])
    message = "No sides equal 0"
    result = size_side_is_zero.check_is_not_zero(size_side_is_zero.size_side)
    assert result != [], message


@pytest.mark.negative_triangle
def test_size_side_is_not_num():
    size_side_not_num = Triangle(0, [20, 60, '50'], [9, 0, 30])
    message = "All of the sides is numbers"
    result = size_side_not_num.check_is_num(size_side_not_num.size_side)
    assert result != [], message


@pytest.mark.negative_triangle
def test_size_side_less_than_zero():
    less_than_zero = Triangle('a', [-10, 0, 50], [-20, 180, 20])
    message = "All sides of the rectangle are greater than 0"
    result = less_than_zero.check_less_than_zero(less_than_zero.size_side)
    assert result != 0, message


@pytest.mark.positive_triangle
def test_correct_angles():
    correct_angles = Triangle(3, [10, -10, 50], [80, 40, 60])
    message = "The size of the angles in the triangle is not correct"
    assert correct_angles.sum_angles_triangle() == SUM_ANGLES, message


@pytest.mark.negative_triangle
def test_angle_is_zero():
    angle_is_zero = Triangle('a', [10, 0, 50], [0, 150, 30])
    message = "No angle equal 0"
    result = angle_is_zero.check_is_not_zero(angle_is_zero.angles)
    assert result != [], message


@pytest.mark.negative_triangle
def test_angle_is_not_num():
    angle_is_not_num = Triangle('a', [10, 0, 50], [20, '125', 35])
    message = "All of the angles is numbers"
    result = angle_is_not_num.check_is_num(angle_is_not_num.angles)
    assert result != [], message


@pytest.mark.negative_triangle
def test_angle_less_than_zero():
    less_than_zero = Triangle('a', [10, 0, 50], [-20, 180, 20])
    message = "All angles of the rectangle are greater than 0"
    result = less_than_zero.check_less_than_zero(less_than_zero.angles)
    assert result != [], message


@pytest.mark.negative_triangle
@pytest.mark.parametrize('count_angle, max_count', [
    (Triangle(3, [30, 60, 40], [120, 30]), MAX_COUNT_TRIANGLE),
    (Triangle(3, [30, 60, 40], [120, 30, 33, 44]), MAX_COUNT_TRIANGLE)])
def test_count_elem_angle(count_angle, max_count):
    message = f"The number of angles is equal to {max_count}"
    result = count_angle.check_count_elem(count_angle.angles)
    assert result != max_count, message


@pytest.mark.positive_triangle
def test_isosceles_triangle_by_sides():
    isosceles_triangle = Triangle(3, [60, 60, 10], [85.22, 85.22, 9.66])
    message = "The number of sides in an isosceles triangle is less than or greater than 2"
    result = isosceles_triangle.check_repeating_elem(isosceles_triangle.size_side)
    assert result == 2, message


@pytest.mark.positive_triangle
def test_isosceles_triangle_by_angles():
    isosceles_triangle = Triangle(3, [60, 60, 10], [85.22, 85.22, 9.66])
    message = "The number of angles in an isosceles triangle is less than or greater than 2"
    result = isosceles_triangle.check_repeating_elem(isosceles_triangle.angles)
    assert result == 2, message


@pytest.mark.positive_triangle
def test_equilateral_triangle_by_sides():
    equilateral_triangle = Triangle(3, [60, 60, 60], [60, 60, 60])
    message = "Sides of an isosceles triangle are not equal"
    result = equilateral_triangle.check_repeating_elem(equilateral_triangle.size_side)
    assert result == 1, message


@pytest.mark.positive_triangle
def test_equilateral_triangle_by_angles():
    equilateral_triangle = Triangle(3, [60, 60, 60], [60, 60, 60])
    message = "Angles of an isosceles triangle are not equal"
    result = equilateral_triangle.check_repeating_elem(equilateral_triangle.angles)
    assert result == 1, message
